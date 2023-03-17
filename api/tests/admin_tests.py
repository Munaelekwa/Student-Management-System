import unittest
from .. import create_app
from ..config.config import config_dict
from ..db import db
from ..models.users import Admin
from ..models.students import Student
from flask_jwt_extended import create_access_token

class UserTestCase(unittest.TestCase):
    
    def setUp(self):

        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()
        

    def tearDown(self):

        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def test_admin(self):

        # Register an admin
        admin_signup_data = {
            "first_name": "Test",
            "last_name": "Admin",
            "email": "testadmin@demo.com",
            "password": "password"
        }

        response = self.client.post('/auth/register', json=admin_signup_data)

        admin = Admin.query.filter_by(email='testadmin@demo.com').first()

        assert admin.name == "Test Admin"

        assert response.status_code == 201
        

        # Sign an admin in
        admin_login_data = {
            "email":"testadmin@demo.com",
            "password": "password"
        }
        response = self.client.post('/auth/login', json=admin_login_data)

        assert response.status_code == 201

        token = create_access_token(identity=admin.id)

        headers = {
            "Authorization": f"Bearer {token}"
        }


        # Register a student
        student_register_data = {
            "first_name": "Test",
            "last_name": "Student",
            "email": "munaelekwa@gmail.com"
        }
        response = self.client.get('/auth/register/student', headers=headers, json=student_register_data)

        student = Student.query.filter_by(email='munaelekwa@gmail.com').first()

        assert student.name == "Test Student"
        assert response.status_code == 200


        # Retrieve a student's details by ID
        response = self.client.get('/admin/student2', headers=headers)

        assert response.status_code == 200

        assert response.json == {
            "id": 2,
            "name": "Test Student",
            "email": "munaelekwa@gmail.com",
            "reg_no": "2023/STD1"
        }


