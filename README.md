# Flask REST API Project

A simple REST API built with Flask, Flask-RESTful, and SQLAlchemy for user management.

## Project Setup

1. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment

# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt:
.\venv\Scripts\activate

# On Unix or MacOS:
source venv/bin/activate
```

2. Install required packages:
```bash
pip install flask
pip install flask_restful
pip install flask_sqlalchemy
```

3. Generate requirements.txt:
```bash
pip freeze > requirements.txt
```

## Project Structure

```
flask-api/
├── venv/
├── app.py
├── requirements.txt
└── README.md
```

## Testing API Endpoints with Postman

### GET Request
- URL: `http://localhost:5000/api/users`
- Method: `GET`
- Description: Retrieves all users
- Expected Response: List of users in JSON format

### GET Single User
- URL: `http://localhost:5000/api/users/<id>`
- Method: `GET`
- Description: Retrieves a specific user by ID
- Expected Response: Single user in JSON format

### POST Request
- URL: `http://localhost:5000/api/users`
- Method: `POST`
- Headers: 
  - Content-Type: `application/json`
- Body:
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}
```
- Description: Creates a new user
- Expected Response: Created user details

### PUT Request
- URL: `http://localhost:5000/api/users/<id>`
- Method: `PUT`
- Headers:
  - Content-Type: `application/json`
- Body:
```json
{
    "name": "John Smith",
    "email": "john.smith@example.com",
    "age": 31
}
```
- Description: Updates an existing user
- Expected Response: Updated user details

### DELETE Request
- URL: `http://localhost:5000/api/users<id>`
- Method: `DELETE`
- Description: Deletes a specific user
- Expected Response: Success message

## Common HTTP Status Codes

- 200: OK (Successful request)
- 201: Created (Successfully created new resource)
- 404: Not Found (Resource doesn't exist)
- 400: Bad Request (Invalid input)
- 500: Internal Server Error

## Development

1. Create `app.py` with your Flask application code
2. Run the development server:
```bash
python app.py
```
3. The API will be available at `http://localhost:5000`

## Dependencies

- Flask: Web framework
- Flask-RESTful: REST API framework
- Flask-SQLAlchemy: SQL ORM for Flask

## Notes

- Make sure to activate the virtual environment before running the application
- Use Postman or similar tools to test API endpoints
- Keep your `requirements.txt` updated when adding new dependencies