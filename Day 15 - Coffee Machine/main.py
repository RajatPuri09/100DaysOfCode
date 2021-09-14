import data
from coffee_shop_functions import report, check_resources, make_coffee, process_coins, transaction, resource
take_order = True

while take_order:
    order = input("What would you like? (Cappuccino/ Espresso/ Latte) \n")
    if order == 'cappuccino':
        if check_resources(data.MENU[order]['ingredients']):
            money_r = process_coins()
            transaction(money_r, order)
            make_coffee(reserve=resource, order_placed=order)
            print(f"Enjoy your {order}!")

    elif order == 'espresso':
        if check_resources(data.MENU[order]['ingredients']):
            data.MENU[order]['ingredients']["milk"] = 0
            money_r = process_coins()
            transaction(money_r, order)
            make_coffee(reserve=resource, order_placed=order)
            print(f"Enjoy your {order}!")

    elif order == 'latte':
        if check_resources(data.MENU[order]['ingredients']):
            money_r = process_coins()
            transaction(money_r, order)
            make_coffee(reserve=resource, order_placed=order)
            print(f"Enjoy your {order}!")

    elif order == 'report':
        report(resource)

    elif order == 'off':
        print("Shutting down. Bye bye!")
        take_order = False

    else:
        print("Invalid input")

