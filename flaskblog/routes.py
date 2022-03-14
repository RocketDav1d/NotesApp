from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LogInForm


posts = [
    {
        "author": "Corey",
        "title" : "blog Post 1",
        "content": "first post content "
    }
    ,
    {
        "author": "Mike",
        "title" : "blog Post 2",
        "content": "second post content "
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts )


@app.route("/about")
def about():
    return render_template("about.html", title="About")
 
 
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() == True:
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f"Acount created for {form.username.data}! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login(): 
    form = LogInForm()
    if form.validate_on_submit() == True:
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"Login of {form.email.data} was succesful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccesful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)






