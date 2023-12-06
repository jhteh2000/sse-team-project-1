from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import json
from functions.results import process_search, get_response
from functions.userbaseAPI import add_row_to_table, return_data, return_user
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functions.userclass import User
from datetime import timedelta

# Flask app configuration
app = Flask(__name__)
app.secret_key = "icptrlAM4HuEBWdcsHDBqedr9dOxeX72"

# Setting up flask login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    user_data = return_user(user_id)
    if user_data:
        user = User(user_data[0]['user_id'], user_data[0]['first_name'], user_data[0]['last_name'], user_data[0]['username (email)'], user_data[0]['password'])
    else:
        user = None
    return user

# All flask routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    args = {}
    args["diet"] = request.form.getlist("diet")
    args["health"] = request.form.getlist("health")
    args["cuisine"] = request.form.getlist("cuisine")
    args["dish"] = request.form.getlist("dish")

    return redirect(url_for("results", args_dict=json.dumps(args)))


@app.route("/results")
def results():
    # Retrieve args_dict from the URL parameters and convert JSON string to dict
    args_dict = request.args.get("args_dict")
    args_dict = json.loads(args_dict)

    # For Testing (Will be replaced with Requests)
    with open("../samplejson/recipe.json", "r") as read_file:
        data = json.load(read_file)

    # For Production
    # response = get_response(args_dict)
    # data = response.json()

    result_args = {
        "count": 0,
        "image": [],
        "name": [],
        "calories": [],
        "protein": [],
        "ingredient": [],
        "recipeURL": [],
    }

    for recipe in data["hits"]:
        if process_search(args_dict, recipe):
            result_args["image"].append(recipe["recipe"]["image"])
            result_args["name"].append(recipe["recipe"]["label"])
            result_args["calories"].append(
                round(
                    recipe["recipe"]["totalNutrients"]["ENERC_KCAL"]["quantity"],
                    ndigits=3,
                )
            )
            result_args["protein"].append(
                round(
                    recipe["recipe"]["totalNutrients"]["PROCNT"]["quantity"], ndigits=3
                )
            )
            result_args["ingredient"].append(recipe["recipe"]["ingredientLines"])
            result_args["recipeURL"].append(recipe["recipe"]["url"])
            result_args["count"] += 1

    return render_template("results.html", result_args=result_args)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated is False:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            
            # Retrieve user data from the database
            user_data = return_data("LoginInfo", email)
            if user_data:
                user = User(user_data[0]['user_id'], user_data[0]['first_name'], user_data[0]['last_name'], user_data[0]['username (email)'], user_data[0]['password'])
                if check_password_hash(user.password, password):
                    login_user(user, duration=timedelta(days=1))
                    next = request.args.get("next")
                    flash("You are logged in!")
                    return redirect(next or url_for("index"))
                flash("Invalid Password")
            flash("User Not Found")
        return render_template("login.html")
    else:
        return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")

        data_to_insert = {
            "first_name": firstName,
            "last_name": lastName,
            "username (email)": email,
            "password": generate_password_hash(password),
        }

        add_row_to_table("LoginInfo", data_to_insert)

        return render_template("registration_success.html", name=firstName)
    return render_template("register.html")

@app.route("/user_info")
@login_required
def user_info():
    
    user_data = return_data("LoginInfo", "yugene524@gmail.com")
    user_first_name = user_data[0]["first_name"]
    user_last_name = user_data[0]["last_name"]
    user_username = user_data[0]["username (email)"]

    #user_favourite_data = return_data("Favorites", "yugene524@gmail.com")
    #for item in user_favourite_data:

    data_to_show = {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_username
    }
    return render_template("userInfo.html", **data_to_show)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for("index"))