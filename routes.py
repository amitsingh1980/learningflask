from flask import Flask, render_template, request
from forms import SignupForm
from models import db

tasker = Flask(__name__)
tasker.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
tasker.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
tasker.secret_key = "development-key"
db.init_app(tasker)

@tasker.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@tasker.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@tasker.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        return "Success !!"
    elif request.method == "GET":
        form = SignupForm()
        return render_template('signup.html', form=form)

if __name__ == "__main__":
    tasker.run(debug=True)