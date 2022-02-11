from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import owner


class Dog:
    db_name = "jan_pet_hospital"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None  # placeholoder to put a user object later

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        # make a connection
        results = connectToMySQL(cls.db_name).query_db(
            query)  # list of dictionaries

        # create a list to hold dog objects
        all_dogs = []
        # go through each dictionary is results
        for row in results:
            # make a dog object using the info from the row (dict)
            dog_object = cls(row)
            # append that dog object to the list "all_dogs"
            all_dogs.append(dog_object)

            # all_dogs.append(cls(row))

        return all_dogs  # list of objects

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dogs(name, age, breed, owner_id) VALUES(%(name)s, %(age)s, %(breed)s, %(owner_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)


    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dogs JOIN owners ON owners.id = owner_id WHERE dogs.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # make a dog object
        this_dog = cls(results[0])
        # make a dict for the owner
        owner_info = {
            'id': results[0]['owners.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'email': results[0]['email'],
            'created_at': results[0]['owners.created_at'],
            'updated_at': results[0]['owners.updated_at'],
        }
        # make an owner object using that information
        this_owner = owner.Owner(owner_info)

        # associate the dog with it's owner using the attribute "owner"
        this_dog.owner = this_owner

        # return the dog object

        return this_dog

