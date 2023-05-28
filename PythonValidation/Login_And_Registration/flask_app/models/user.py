from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re # the regex module

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

DATABASE = 'login_reg'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM users 
            WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return User(results[0])
        else:
            return False

    
    @staticmethod
    def validate_user_info(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Required field")
            is_valid = False
            flash("Required field")
        if not EMAIL_REGEX.match(user['email']):
            flash("Required field","email")
            is_valid = False
        if user['password'] != user['confirm-password']:
            is_valid = False
            flash("Password doesn't match", 'confirm-password') #setting a catgory "password" and will flash password
        if len(user['password']) < 8:
            is_valid = False
            flash("Create a secure password. Your password must be at least 8 or more characters.", 'password') #setting a catgory "password" and will flash password to short
        print(is_valid)
        return is_valid
        
        
        