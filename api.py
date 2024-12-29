#Code includes that REST API services

#flask web framework imported
from flask import Flask

#ORM for connect python code
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

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

#When arguments passing to the functions given fields can't be null(means arguments passing should completed)
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")

#Defining the user's data fields
userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String,
}

#Getting the users
class Users(Resource):
    #marshaling(decorating) allows to send the stored user data in the json format
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all() 
        return users 

    #marshaling(decorating) using to store users to database table
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user) 
        db.session.commit()
        users = UserModel.query.all()
        #user successfully added response
        return users, 201
        api.add_resource(Users, '/api/users/')

#If the entered id doesn't match with the existing ids error meassage shown
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        return user 
    

    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

    
#route for the home page
@app.route('/')

def home():
    return '<h1> REST API from flask <h1>'

if __name__ == '__main__':
    app.run(debug=True)

