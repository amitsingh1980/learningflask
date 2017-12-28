from flask import Flask, render_template, request
from forms import SignupForm
from models import db, User

tasker = Flask(__name__)
#postgres://atlxhdlrnkajnh:6e235273ac61d8e42912823e632018f715f24d1807df14ec098cccf4b9a0b00c@ec2-54-163-233-103.compute-1.amazonaws.com:5432/ddnftacagsaq27
#postgresql://localhost/learningflask
tasker.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://atlxhdlrnkajnh:6e235273ac61d8e42912823e632018f715f24d1807df14ec098cccf4b9a0b00c@ec2-54-163-233-103.compute-1.amazonaws.com:5432/ddnftacagsaq27'
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
    form = SignupForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.Name.data, form.Email.data, form.Address.data)
            db.session.add(newuser)
            db.session.commit()
            return "Success !!"
    elif request.method == "GET":
        return render_template('signup.html', form=form)

if __name__ == "__main__":
    tasker.run(debug=True)