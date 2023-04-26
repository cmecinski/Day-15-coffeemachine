MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


coffee_on = True

def coin_transaction():
    """ Returns total value of inserted coins"""
    print("Please insert coins.")
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.10
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount

def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made, False if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
    return True


def check_transaction(money_received, drink_cost):
    """Return True if payment is accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



while coffee_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if input == "off":
        coffee_on = False
    elif prompt == "report":
        print(f" Water: {resources['water']}ml ")
        print(f" Milk: {resources['milk']}ml ")
        print(f" Coffee: {resources['coffee']}g ")
        print(f" Money: ${resources['money']} ")
    else:
        drink = MENU[prompt]
        if is_resource_sufficient(drink["ingredients"]):
            value = coin_transaction()
            if check_transaction(value, drink["cost"]):
                make_coffee(prompt, drink["ingredients"])