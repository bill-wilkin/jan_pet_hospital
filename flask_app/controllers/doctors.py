from flask_app import app
from flask import render_template, redirect, request

# doctors

# # /dogs  --                 localhost:5000/dogs     GET
# @app.route('/doctors')
# def show_all_dogs():
#     return render_template("doctors.html")

# # /doctors/new                 localhost:5000/doctors/new   GET  
# @app.route('/doctors/new')
# def new_dog_form():
#     return render_template("new_dog.html")

# # /doctors/create              localhost:5000/doctors/create  POST 
# @app.route("/doctors/create", methods = ["POST"])
# def create_dog():
    
#     return redirect("/")

# # /doctors/<int:dog_id>        localhost:5000/doctors/800  GET
# @app.route('/doctors/<int:dog_id>')
# def dog_profile(dog_id):
#     return render_template("dog_profile.html")

# # /doctors/<int:dog_id>/edit   localhost:5000/doctors/800/edit  GET

# @app.route('/doctors/<int:dog_id>/edit')
# def edit_dog_page():
#     return render_template("edit_dog.html")

# # /dogs/<int:dog_id>/update   localhost:5000/dogs/800/update  POST
# @app.route('/dogs/<int:dog_id>/update', methods = ["POST"])
# def update_dog():
    
#     return redirect("/")


# # /dogs/<int:dog_id>/delete   localhost:5000/dogs/800/delete  GET

# @app.route('/dogs/<int:dog_id>/delete')
# def delete_dog_page():
#     return render_template('delete_dog_page.html')

# # /dogs/<int:dog_id>/destroy   localhost:5000/dogs/800/destroy  POST

# @app.route("/dogs/<int:dog_id>/destroy", methods = ["POST"])
# def delete_dog():
    
#     return redirect("/")
