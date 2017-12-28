from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm, LoginForm
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
            session['email'] = newuser.Email
            return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template('signup.html', form=form)

@tasker.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    else:    
        return render_template("home.html")

@tasker.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        validated = form.validate()
        if validated == False:
            return render_template("login.html", form=form)
        else:
            email = form.Email.data        
            user = User.query.filter_by(Email=email).first()
            
            if user is not None:
                session['email'] = form.Email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template("login.html", form=form)

@tasker.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))
    

if __name__ == "__main__":
    tasker.run(debug=True)

