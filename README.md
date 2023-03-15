# Student-Management-System

Note: This is currently under active development

## Table of Contents

- [Student Management System](#student-management-system)
  - [Table of Contents](#table-of-contents)
  - [Live ( deployed version )](#live--deployed-version-)
  - [Testing Locally](#testing-locally)
  - [Available Endpoints](#available-endpoints)
    - [Auth Endpoint](#auth-endpoint)
    - [Students Endpoint](#students-endpoint)
    - [Admin Endpoint](#admin-endpoint)

## Live ( deployed version ) 

Visit [website](http://olakaycoder1.pythonanywhere.com/)
## Testing Locally

Clone the repository

```console
git clone https://github.com/Munaelekwa/Student-Management-System.git
```

Change directory to the cloned folder

```console
cd Student-Management-System
```

Install necessary dependencies to run the project

```console
pip install -r requirements.txt
```
Create database from migration files 

```console
flask db migrate -m "your description"
```

```console
flask db upgrade
```
Run application

```console
flask run
```
To test routes:

- Create a new admin account with the auth/register route. Registration code for creating admin (reg_code) is 'ADM990'. 
- Log in with admin email and password and copy access token
- Enter access token in the authorization header as bearer
- Proceed to test out admin functions ie create new students, create new courses, delete students etc
- Log in as a student (note: use a valid email address to create the student account to enable you recieve the login password)
- Test out student functions ie register courses, calculate gpa etc

Continue testing......



## Available Endpoints

### Auth Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `auth/register` | _POST_ | It allows the  creation of an admin account   | Any | Any |  ---- | 
|  `auth/register/student` |  _POST_ | It allows an admin create a student account   | Authenticated | Admin | ---- | 
|  `auth/login` |  _POST_  | It allows user authentication   | Any | Any | ---- | 
|  `auth/login/refresh` |  _POST_  | It allows user refresh their tokens   | Authenticated | Any | ---- | 


### Students Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `students/courses/grade` |  _GET_  | It allows student retrieve all registered courses grade | Authenticated | Student | ---- |
|  `students/courses` |  _GET_  | It allows the retrieval of a student courses   | Authenticated | ---- | A student ID |
|  `students/gpa` |  _GET_  | Calculate a student gpa score   | Authenticated | Any | A student ID |
|  `students/courses/add_and_drop` |  _POST_  | It allows student register a course   | Authenticated | Student | ---- |
|  `students/courses/add_and_drop` |  _DELETE_  | It allows student unregister a course   | Authenticated | Student | ---- |



### Admin Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `admin/courses` |  _GET_  | It allows the retrieval of all available courses   | Authenticated | Any | ---- |
|  `admin/courses` |  _POST_  | It allows the creation of a new course   | Authenticated | Admin | ---- |
|  `admin/courses/<course_id>` |  _DELETE_  | It allows deleting a course   | Authenticated | Admin | ---- |
|  `admin/courses/<course_id>` |  _GET_  | It allows the retrieval of a particular course   | Authenticated | Admin | A course ID |
|  `admin/course<course_id>/students` |  _GET_  | It allows the  retrieval of all students registered for a course | Authenticated | Admin | A course ID |
|  `admin/course<course_id>/students/add_and_drop` |  _POST_  | It allows admin to add a student to a course | Authenticated | Admin | A course ID |
|  `admin/course<course_id>/students/add_and_drop` |  _DELETE_  | It allows admin to remove a  student from a course | Authenticated | Admin | A course ID |
|  `admin/student<student_id>` |  _GET_  | It allows admin to retrieve a particular student | Authenticated | Admin | A Student ID |
|  `admin/student<student_id>` |  _DELETE_  | It allows admin to remove a particular student | Authenticated | Admin | A Student ID |
|  `admin/all_students` |  _GET_  | It allows admin to retrieve all students in the school | Authenticated | Admin | ---- |
|  `admin/student/course/add_score` |  _PUT_  | It allows admin add a student score in a course | Authenticated | Admin | A course ID, A student ID |
|  `admin/student<student_id>/courses/grade` |  _GET_  | It allows the admin retrieve a student all courses grade   | Authenticated | Admin | A student ID |
