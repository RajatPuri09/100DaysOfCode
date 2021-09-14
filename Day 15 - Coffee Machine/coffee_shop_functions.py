import data
resource = data.resources
resource['money'] = 0


def report(reserve):
    print(
        f" Water: {reserve['water']}\n Milk: {reserve['milk']}\n Coffee: {reserve['coffee']} \n Money: {reserve['money']} $")


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry not enough {item}")
            return False
        else:
            return True


def make_coffee(reserve, order_placed):
    reserve['water'] = reserve['water'] - data.MENU[order_placed]['ingredients']["water"]
    reserve['milk'] = reserve['milk'] - data.MENU[order_placed]['ingredients']["milk"]
    reserve['coffee'] = reserve['coffee'] - data.MENU[order_placed]['ingredients']["coffee"]
    reserve['money'] = reserve['money'] + data.MENU[order_placed]["cost"]
    return reserve


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(money_received, order_placed):
    if money_received >= data.MENU[order_placed]["cost"]:
        change = (money_received - data.MENU[order_placed]["cost"]).__round__(2)
        print(f"Here is your ${change} change")
    else:
        print("The money received was not enough. You have been refunded")