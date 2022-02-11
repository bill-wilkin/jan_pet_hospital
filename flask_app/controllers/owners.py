from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import owner
import pprint

#render our users page
@app.route('/') #root route
def index():   
    # session.clear()        #file class  method
    owners_from_database = owner.Owner.get_all() #list of objects
    pprint.pprint(owners_from_database)
    print(f'What is in session so far: {session}')
    return render_template('index.html', all_owners = owners_from_database)


@app.route("/owners/create", methods = ["POST"])
def create_owner():
    print(f"REQUEST FORM: {request.form}")
    new_owner = owner.Owner.create_owner(request.form)
    
    return redirect("/")
# @app.route('/owners/<int:owner_id>')
# def owner_profile(owner_id): #get or post
#     info_dict = {
#         'id':owner_id
#     }
#     this_owner = owner.Owner.get_one_by_id(info_dict) #one owner object
#     session['email']= this_owner.email
    
    return render_template('owner_profile.html', owner = this_owner)

@app.route("/owners/<int:owner_id>/update", methods = ["POST"])
def edit_owner(owner_id):
    data_dictionary = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id': owner_id
    }
    owner.Owner.edit_owner(data_dictionary)

    # return redirect("/")
    #redirect to owner profile /owners/3
    return redirect(f"/owners/{owner_id}")

@app.route("/owners/<int:owner_id>/destroy", methods = ["POST"])
def destroy_owner(owner_id):
    data_dictionary = {
        'id': owner_id
    }
    owner.Owner.destroy_owner(data_dictionary)
    return redirect("/")

@app.route('/owners')
def owners():
    owners_from_db = owner.Owner.get_all()
    return render_template('owners.html', all_owners = owners_from_db)

@app.route('/owners/<int:owner___id>')
def owner_profile(owner___id):
    owner_info = {
        'id':owner___id
    }
    that_owner = owner.Owner.get_one_with_dogs(owner_info)
    return render_template('owner_profile.html', this_owner =that_owner)
