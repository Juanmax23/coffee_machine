from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofe_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    option = menu.get_items()
    chocie = input(f"What would you like? ({option}): ")
    if chocie == "off":
        is_on = False
    elif chocie == "report":
        cofe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(chocie)
        if cofe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cofe_maker.make_coffee(drink)

