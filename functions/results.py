def process_search(args_dict, recipeJSON):
    result = []

    result.append(all(diet in recipeJSON["recipe"]["dietLabels"] for diet in args_dict["diet"]))
    result.append(all(health in recipeJSON["recipe"]["healthLabels"] for health in args_dict["health"]))
    result.append(all(cuisine in recipeJSON["recipe"]["cuisineType"] for cuisine in args_dict["cuisine"]))
    result.append(all(dish in recipeJSON["recipe"]["dishType"] for dish in args_dict["dish"]))

    return all(result)