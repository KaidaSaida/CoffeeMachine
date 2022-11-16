from data import MENU
from data import resources

resources['money'] = 0


def report():
    """ Prints the remaining resources in the machine """

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


off = False

while not off:
    QUARTER = 0.25
    DIME = 0.10
    NICKEL = 0.05
    PENNY = 0.01
    total = 0

    def resource_check(order_resources):
        """Compares the menu requirements to the resources"""

        for ingredients in MENU[order_resources]['ingredients']:
            ingredient = MENU[order_resources]['ingredients'][ingredients]
            if ingredient > resources[ingredients]:
                print(f"Sorry there is not enough {ingredients}")
                return False
            else:
                return True


    def payment():
        """Counts amount of coins given and returns total payment"""
        coins = []
        print("Please insert coins.")
        quarters_pd = int(input("How many quarters?: "))
        coins.append(quarters_pd * QUARTER)

        dimes_pd = int(input("How many dimes?: "))
        coins.append(dimes_pd * DIME)

        nickels_pd = int(input("How many nickels?: "))
        coins.append(nickels_pd * NICKEL)

        pennies_pd = int(input("How many pennies?: "))
        coins.append(pennies_pd * PENNY)

        paid = sum(coins)
        return paid


    def reduce_resources(order_to_reduce):
        """Reduces the resources by the amount in the order"""
        global resources
        for ingredient in MENU[order_to_reduce]['ingredients']:
            reduce = MENU[order_to_reduce]['ingredients'][ingredient]
            resources[ingredient] -= reduce


    def change_check(total_for_change, cost):
        """Calculates if enough paid. Returns amount if yes, False if no"""
        if total_for_change >= cost:
            change = total_for_change - cost
            return round(change, 2)
        else:
            print("Sorry that's not enough money")
            return False


    def process_order():
        """Processes the order, deducts resources, and adds money."""
        global total
        global off
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'off':
            off = True

        elif order == 'report':
            report()
        else:
            cost = MENU[order]['cost']

            can_run = resource_check(order)
            if can_run:
                total = payment()
                change = change_check(total, cost)
                if change >= 0:
                    resources['money'] += round(total - change, 2)
                    reduce_resources(order)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {order} ☕. Enjoy!")
    process_order()