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
    names = []   
    for food in spicy_foods:
        names.append(food["name"])    
    return names
    

def get_spiciest_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spicy.append(food)
    return spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        chilli = "🌶" * food['heat_level']
        heat = food['heat_level']
        if heat > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {chilli}")
        
def get_average_heat_level(spicy_foods):
    heat = sum(food['heat_level'] for food in spicy_foods)
    total = len(spicy_foods)
    return heat / total

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
