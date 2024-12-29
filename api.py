#Code includes that REST API services

#flask web framework imported
from flask import Flask

#ORM for connect python code
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#Connecting with the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) 
api = Api(app)

#User model fields defining
class UserModel(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

#function for returning the stored user model data
    def __repr__(self): 
        return f"User(name = {self.name}, email = {self.email})"

#route for the home page
@app.route('/')

def home():
    return '<h1> REST API from flask <h1>'

if __name__ == '__main__':
    app.run(debug=True)

