# Notes App

## Overview

The Notes App is a Django-based application designed to help users manage their notes. It supports user authentication and CRUD (Create, Read, Update, Delete) operations for notes. The application also features an admin interface for managing users and notes.

## Features

- User authentication (login and logout)
- CRUD operations for managing notes
- Admin interface for managing users and notes
- REST API for notes and users management

## Prerequisites

To run this project locally, ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:
```
git clone https://github.com/maria.v.ch/notes_app_rep.git
cd notes_app
```

### 2. Create and Activate a Virtual Environment
It's a good practice to use a virtual environment to manage your project's dependencies. Create and activate a virtual environment with the following commands: `python -m venv venv`

- **Windows:**
  `venv\Scripts\activate`
- **macOS and Linux:**
  `source venv/bin/activate`

### 3. Install Dependencies
Install the required Python packages using pip: `pip install -r requirements.txt`.

### 4. Set Up Environment Variables
Create an .env file in the root directory of the project to store environment-specific variables. Use the provided .env example as a reference:
```
DEBUG=True
SECRET_KEY=your-secret-key
```
Replace your-secret-key with a secure secret key. You can generate a new one using Django's secret key generator.

### 5. Apply Database Migrations
Run the following command to apply the database migrations:
`python manage.py migrate
`.
### 6. Create a Superuser
To access the Django admin interface, create a superuser: `python manage.py createsuperuser`. Follow the prompts to enter a username, email, and password.

### 7. Run the Development Server
Start the Django development server: `python manage.py runserver`. The server will start running on http://127.0.0.1:8000/. You can now open this URL in your browser to access the application.

## Usage
### API Endpoints
#### User Management Endpoints (Admin Only):
- List Users: **GET /api/admin/users/**
- Retrieve User: **GET /api/admin/users/<int:pk>/**
- Create User: **POST /api/admin/users/**
- Update User: **PUT /api/admin/users/<int:pk>/**
- Delete User: **DELETE /api/admin/users/<int:pk>/**
        
#### Notes Management Endpoints:
- List Notes: **GET /api/notes/**
- Retrieve Note: **GET /api/notes/<int:pk>/**
- Create Note: **POST /api/notes/**
- Update Note: **PUT /api/notes/<int:pk>/**
- Delete Note: **DELETE /api/notes/<int:pk>/**
  
### Admin Interface
Access the Django admin interface at **http://127.0.0.1:8000/admin** and log in using the superuser credentials created earlier.

## Running Tests
To run the tests for this project, use the following command: `python manage.py test`. This will execute the test cases defined in the notes/tests.py file and report any issues.

## Additional Information
### Static Files
Django will automatically handle static files during development. In a production environment, ensure that static files are properly configured.

### Deployment
For deploying to a production environment, consider using a production-grade server like Gunicorn or uWSGI along with a web server like Nginx. Configure the database, static files, and environment variables as needed for production.

## Contributing
Feel free to fork this repository and submit pull requests for enhancements or bug fixes. Contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.








