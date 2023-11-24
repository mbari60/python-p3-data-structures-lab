spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
       for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🥕' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        #checking if the cuisine in the spicy foods matches the cuisine that user inputs 
        if food["cuisine"].lower() == cuisine.lower():
            return food

def print_spiciest_foods(spicy_foods):
     #i did note that i had foods with heatlevel more than 5 so i called the function and stored the foods in spiciest_foods 
    spiciest_foods = get_spiciest_foods(spicy_foods)
    #i did note that i had the format needed on printing spicy food so i just called the function and passed the spiciest food as an argument so that it will be printed in the same format
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    if spicy_foods:
        total_heat_level = sum(food["heat_level"] for food in spicy_foods)
        average_heat_level = total_heat_level // len(spicy_foods)
        return average_heat_level
    else:
        return 0    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

