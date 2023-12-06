from flask import Flask, render_template, request, redirect, url_for
import json
from functions.results import process_search
from functions.userbaseAPI import add_row_to_table
from functions.userbaseAPI import return_data

app = Flask(__name__)


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
    
    result_args = {"count": 0, "image": [], "name": [], "calories": [], "protein": [], "ingredient": []}

    for recipe in data["hits"]:
        if process_search(args_dict, recipe):
            result_args["image"].append(recipe["recipe"]["image"])
            result_args["name"].append(recipe["recipe"]["label"])
            result_args["calories"].append(round(recipe["recipe"]["totalNutrients"]["ENERC_KCAL"]["quantity"], ndigits=3))
            result_args["protein"].append(round(recipe["recipe"]["totalNutrients"]["PROCNT"]["quantity"], ndigits=3))
            result_args["ingredient"].append(recipe["recipe"]["ingredientLines"])
            result_args["count"] += 1

    return render_template("results.html", result_args=result_args)

@app.route("/login")
def login():
    return render_template("login.html")

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
            "password": password,
        }

        add_row_to_table("LoginInfo", data_to_insert)

        return render_template("registration_success.html", name=firstName)
    return render_template("register.html")

@app.route("/user_info")
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
