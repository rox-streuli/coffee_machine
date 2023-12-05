from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

till = MoneyMachine()
menu_choices = Menu()
cafetera = CoffeeMaker()

turn_off_machine = False
while not turn_off_machine:
    print(f"What would you like? {menu_choices.get_items()}")
    user_choice = input("--> ")
    # Turn off the Coffee Machine by entering “off”
    if user_choice == 'off':
        turn_off_machine = True
    elif user_choice == 'report':
        print("*" * 13)
        cafetera.report()
        till.report()
        print("*" * 13)
    else:
        user_order = menu_choices.find_drink(user_choice)
        if user_order == None:
            continue
        else:
            if cafetera.is_resource_sufficient(user_order):
                print("-" * 30)
                success = till.make_payment(user_order.cost)
                print("-" * 30)
                if success:
                    cafetera.make_coffee(user_order)
                    print()

print("\nTurning off coffee machine...")