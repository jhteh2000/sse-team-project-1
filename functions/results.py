import requests
import os


def process_search(args_dict, recipeJSON):
    result = []

    result.append(
        all(diet in recipeJSON["recipe"]["dietLabels"] for diet in args_dict["diet"])
    )
    result.append(
        all(
            health in recipeJSON["recipe"]["healthLabels"]
            for health in args_dict["health"]
        )
    )
    result.append(
        all(
            cuisine in recipeJSON["recipe"]["cuisineType"]
            for cuisine in args_dict["cuisine"]
        )
    )
    result.append(
        all(dish in recipeJSON["recipe"]["dishType"] for dish in args_dict["dish"])
    )

    return all(result)


def get_response(args_dict):
    edamam_api = (
        "https://api.edamam.com/api/recipes/v2?type=public&app_id="
        + os.getenv("EDAMAM_APP_ID")
        + "&app_key="
        + os.getenv("EDAMAM_APP_KEY")
    )

    for diet in args_dict["diet"]:
        edamam_api += "&diet=" + str.lower(diet)

    for health in args_dict["health"]:
        edamam_api += "&health=" + str.lower(health)
    
    for cuisine in args_dict["cuisine"]:
        edamam_api += "&cuisineType=" + cuisine
    
    for dish in args_dict["dish"]:
        edamam_api += "&dishType=" + dish
    
    return requests.get(edamam_api)
