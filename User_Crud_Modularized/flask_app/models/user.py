from flask_app.config.mysqlconnection import connectToMySQL

#The model section is where we write our classes 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #This class method is creatina function that will retrieve all user from are sql table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user').query_db(query)

        #Will create an empty list and append the users we create into that list
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('user').query_db(query, data)
        if result:
            return cls(result[0]) #results is a list in python 
        return False

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email) 
        VALUES 
        (%(first_name)s, %(last_name)s, %(email)s);
        """
        
        #This line will insert are value we create from are form into are database
        results = connectToMySQL('user').query_db(query,data)
        return results

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET first_name = %(first_name)s, last_name =%(last_name)s, 
        email=%(email)s, updated_at =NOW() WHERE id =%(id)s
        """
        return connectToMySQL('user').query_db(query,data)

    @classmethod
    def delete_user(cls, data):
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """
        return connectToMySQL('user').query_db(query,data)