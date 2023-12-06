from flask import Flask, render_template, request, redirect, url_for
import json
from functions.results import process_search, get_response

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


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")
