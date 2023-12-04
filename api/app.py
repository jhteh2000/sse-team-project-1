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
    
    result_args = {"image": [], "name": [], "calories": [], "protein": []}
    for recipe in data["hits"]:
        result_args["image"].append(recipe["recipe"]["image"])
        result_args["name"].append(recipe["recipe"]["label"])
        result_args["calories"].append(round(recipe["recipe"]["totalNutrients"]["ENERC_KCAL"]["quantity"], ndigits=3))
        result_args["protein"].append(round(recipe["recipe"]["totalNutrients"]["PROCNT"]["quantity"], ndigits=3))
        

    return render_template("results.html", result_args=result_args)