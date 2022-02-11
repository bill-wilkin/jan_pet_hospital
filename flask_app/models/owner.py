from turtle import update
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dog

class Owner:
    db_name = "jan_pet_hospital"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dogs = [] #list of dog objects
    
    # instance use self
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    # class methods use cls

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM owners;"
        owners_from_database = connectToMySQL(cls.db_name).query_db(query)

        ######################################################################
        #
        #		GOAL turn a list of dictionaries into a list of objects
        #
        ######################################################################
        list_of_owner_objects = [] #list of ojbects

        #1 go through each dict
        for owner_dict in owners_from_database:

            #2 turn that dict into an obj
            owner_object = cls(owner_dict)
            # owner_object = Owner(owner_dict)
            #3 put that obj into the list "list_of_owner_objects"

            list_of_owner_objects.append(owner_object)
        

        return list_of_owner_objects #list of dictionaries


    #CRUD are class methods
    @classmethod
    def create_owner(cls, data):
        # prepared statement
        query = "INSERT INTO owners (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        owner_id = connectToMySQL(cls.db_name).query_db(query, data)
        return owner_id

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM owners WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # datatype - list of one dictionary
        print(f"RESULTS: {results[0]}")
        # turn one dictionary into object
        return cls(results[0])
    
    # update
    @classmethod
    def edit_owner(cls, data):
        query = "UPDATE owners SET 'first_name' = %(first_name)s, 'last_name'=%(last_name)s, 'email' = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  

    # destroy
    @classmethod
    def destroy_owner(cls, data):
        query = "DELETE FROM owners WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)


    # get_all_with_dogs
    @classmethod
    def get_one_with_dogs(cls, data):
        print(f"DATA:  {data['id']}")
        query = "SELECT * from owners LEFT JOIN dogs ON owners.id = owner_id WHERE owners.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # list of dictionaries
        print(f"RESULTS: {results}")
        # make an owner object
        this_owner = cls(results[0])

        # go through each dog
        for row in results:

        # make a dict for the dog info
            dog_info = {
                'id': row['dogs.id'],
                'name': row['name'],
                'age': row['age'],
                'breed': row['breed'],
                'created_at': row['dogs.created_at'],
                'updated_at': row['dogs.updated_at'],

            }

            # make a dog object with that dog info
            this_dog = dog.Dog(dog_info)

            # put that dog object in the attribute "dogs" of the owner object
            this_owner.dogs.append(this_dog)

        # return the owner object
        return this_owner



    # get_one_with_dogs