from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    args = {}
    args["diet"] = request.form.getlist("diet")
    args["health"] = request.form.getlist("health")
    args["cuisine"] = request.form.getlist("type")
    args["dish"] = request.form.getlist("dish")

    print(args)

    return redirect(url_for("results"))

@app.route("/results")
def results():
    # For Testing (Will be replaced with Requests)
    with open("../samplejson/recipe.json", "r") as read_file:
        data = json.load(read_file)
    
    result_args = {"count": 0,"image": [], "name": [], "calories": [], "protein": []}
    ingredient = []

    for recipe in data["hits"]:
        result_args["image"].append(recipe["recipe"]["image"])
        result_args["name"].append(recipe["recipe"]["label"])
        result_args["calories"].append(round(recipe["recipe"]["totalNutrients"]["ENERC_KCAL"]["quantity"], ndigits=3))
        result_args["protein"].append(round(recipe["recipe"]["totalNutrients"]["PROCNT"]["quantity"], ndigits=3))
        ingredient.append(recipe["recipe"]["ingredientLines"])
        result_args["count"] += 1
        if result_args["count"] > 2:
            break

    # json_data = json.dumps(ingredient)
    json_data = ingredient

    return render_template("results.html", result_args=result_args, json_data=json_data)

# @app.route("<id>/recipe")