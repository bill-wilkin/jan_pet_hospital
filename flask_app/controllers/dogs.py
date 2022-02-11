from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import owner, dog
# from ..models import owner


@app.route("/dogs/new")
def new_dog():
    owners_from_db = owner.Owner.get_all()

    return render_template('new_dog.html', all_owners=owners_from_db)


@app.route("/dogs/create", methods=["POST"])
def create_dog():

    # use class method to make a new dog in the db
    request.form
    new_dog_id = dog.Dog.create(request.form)

    return redirect("/dogs/new")


@app.route('/dogs')
def dogs():
    return render_template('dogs.html', all_dogs=dog.Dog.get_all())


@app.route('/dogs/<int:dog_id>')
def dog_profile(dog_id):
    dog_info = {
        'id': dog_id
    }
    that_dog = dog.Dog.get_by_id(dog_info)
    return render_template("dog_profile.html", this_dog=that_dog)
