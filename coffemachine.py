# Coffee prices
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}

def print_report():
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if amount > resources[ingredient]:
            print(f"\n--Sorry, not enough {ingredient}.--")
            return False
    return True

def process_coins():
    print("\n--Please insert coins.--")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def process_transaction(drink, inserted_money):
    cost = MENU[drink]["cost"]
    if inserted_money >= cost:
        change = round(inserted_money - cost, 2)
        print(f"\n--Here is your change: ${change}--")
        resources["money"] += cost
        return True
    else:
        print("\n--Sorry, that's not enough money. Money refunded.--")
        return False

def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"\nHere is your {drink}. Enjoy!")


while True:
    choice = input("--\nEnter 'report' for print report \nEnter 'Off' to turn off machine\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            money_inserted = process_coins()
            if process_transaction(choice, money_inserted):
                make_coffee(choice)
    else:
        print("Invalid choice. Please try again.")
