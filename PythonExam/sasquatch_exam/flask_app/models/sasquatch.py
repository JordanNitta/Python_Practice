from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from flask_app.models import user
from pprint import pprint

DATABASE = 'sasquatch_sighting'

class Sasquatch:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_sited = data['date_sited']
        self.number_sighted = data['number_sighted']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM sasquatches 
        LEFT JOIN users 
        ON users.id = sasquatches.user_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_sasquatches = []
        for sasquatch in results:
            # recipe instance
            sasquatch_instance = cls(sasquatch)
            #extracting data
            user_data = {
                **sasquatch,
                'id': sasquatch['users.id'],
                'created_at': sasquatch['users.created_at'],
                'updated_at': sasquatch['users.updated_at']
            }
            # creating user instance
            user_instance = user.User(user_data)
            # attaching recipe with user 
            sasquatch_instance.user = user_instance
            # adding them to a list not in get_one 
            all_sasquatches.append(sasquatch_instance)
            # Return recipe all_recipes list which contains all the recipe instance with the user instance attached
        return all_sasquatches

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM sasquatches 
        LEFT JOIN users ON users.id = sasquatches.user_id WHERE sasquatches.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        #1. Create recipe instance
        sasquatch = cls(results[0])
        #2. create user data dict extract user data
        user_data = {
            **results[0],
            'id': results[0]['users.id'],
            'created_at': results[0]['users.created_at'],
            'updated_at': results[0]['users.updated_at']
        }
        #3. create user instance
        # user_instance = user.User(user_data)
        #4. attach to recipe instance the user instance 
        # recipe_instance.user = user_instance
        sasquatch.user = user.User(user_data)
        #5. return recipe instance
        return sasquatch

    @classmethod
    def save_sasquatch(cls, data):
        query = """ 
        INSERT INTO sasquatches (location, what_happened, date_sited, number_sighted, user_id) 
        VALUES (%(location)s, %(what_happened)s, %(date_sited)s, %(number_sighted)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM sasquatches
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE sasquatches
        SET location  = %(location)s, 
        what_happened = %(what_happened)s, 
        date_sited = %(date_sited)s, 
        number_sighted = %(number_sighted)s 
        WHERE sasquatches.id = %(id)s;
        """
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_sasquatch(data):
        is_valid = True
        if len(data['location']) < 3:
            flash('Name needs to be longer then three characters', 'error_location')
            is_valid = False
        if len(data['what_happened']) < 10:
            flash('Description needs to be longer then three characters', 'error_what_happened')
            is_valid = False
        if data['date_sited'] == '':
            flash('Select a date', 'error_date')
        if int(data['number_sighted']) <= 1:
            flash('Number has to be greater then 1', 'error_number')
            is_valid = False
        return is_valid
        