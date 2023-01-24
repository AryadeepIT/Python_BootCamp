from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating object from the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# method calling
money_machine.report()
coffee_maker.report()
menu = Menu()
is_on = True

# while coffee machine is on :
while is_on:
    options = menu.get_items()  # get items method
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
