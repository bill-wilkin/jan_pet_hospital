from flask_app import app
from flask_app.controllers import dogs, doctors, owners

if __name__=="__main__": # are we directly running this file?
    app.run(debug=True, port = 8000) # default to 5000