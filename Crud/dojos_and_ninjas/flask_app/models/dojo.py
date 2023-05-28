from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# from pprint import pprint

DATABASE = 'ninjas_and_dojo_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for dojo in results:
            #making a instance of dojos
            all_dojos.append(cls(dojo))
        return all_dojos


    @classmethod
    def get_all_dojo_ninja(cls, data):
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        # creating an instance based off first dict in that list since all dicts are the same
        dojo = cls(results[0])
        print(results)
        # extradicting the data
        for dict in results:
            ninja_data = {
                'id': dict['ninjas.id'],
                'first_name': dict['first_name'],
                'last_name': dict['last_name'],
                'age': dict['age'],
                'created_at': dict['ninjas.created_at'],
                'updated_at': dict['ninjas.updated_at'],
                'dojo_id': dict['dojo_id']
            }
            # calling the ninja class and passing in the extracted data
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def save_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


    