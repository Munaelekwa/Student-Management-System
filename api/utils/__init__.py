from flask_jwt_extended import get_jwt , verify_jwt_in_request
from functools import wraps
from flask import jsonify
from http import HTTPStatus
from ..models.users import User
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import string
import secrets



sender_email = 'studentmanagementsystem34@gmail.com'
password = 'gidu udsn czkl kigb'

def random_char(length):
    """ Generate a random string 
    param:
        length : length of string to be generated"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

def get_user_type(pk:int):
    """ Get the type a user belong 
    param:
        pk : user id
    """
    user = User.query.filter_by(id=pk).first()
    if user:
        return user.user_type
    return None




def admin_required():
    """
    A decorator to protect an endpoint with JSON Web Tokens.
    Any route decorated with this will require a user type of admin  to be present in the
    request before the endpoint can be called.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args,**kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            print(claims)
            if get_user_type(claims['sub']) == 'admin':
                return fn(*args,**kwargs)
            return jsonify({'msg':"Admin only!"}) , HTTPStatus.UNAUTHORIZED
        return decorator
    return wrapper


def student_required():
    """
    A decorator to protect an endpoint with JSON Web Tokens.
    Any route decorated with this will require a user type of student  to be present in the
    request before the endpoint can be called.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args,**kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if get_user_type(claims['sub']) == 'student' :
                return fn(*args,**kwargs)
            return jsonify({'msg': "Student Only!" }) , HTTPStatus.UNAUTHORIZED
        return decorator
    return wrapper

def get_grade(score):
    """ Convert a score to corresponding grade """
    if score < 100 and score > 89:
        return 'A'
    elif score < 90 and score > 79:
        return 'B'
    elif score < 80 and score > 69:
        return 'C'
    elif score < 70 and score > 59:
        return 'D'
    elif score < 60 and score > 49:
        return 'E'
    elif score < 50 :
        return 'F'    
    else:
        return 'F'


def convert_grade_to_gpa(grade):
    """Convert a grade to the corresponding point value """
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.3
    elif grade == 'C':
        return 2.3
    elif grade == 'D':
        return 1.3
    else:
        return 0.0

class MailServices():
    def student_details_mail(self, student_email , student_name, student_reg_no, student_password ):
        """
        Send a mail containing student details(reg_no, password) to a registered student
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Student Details"
        message["From"] = sender_email
        message["To"] = student_email
        html = (f"Dear {student_name}, \nYou were registered successfully on the student portal. Here are your login details: \nRegistration number: {student_reg_no} \npassword: {student_password}")
        part = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        message.attach(part)
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, student_email, message.as_string()
            )