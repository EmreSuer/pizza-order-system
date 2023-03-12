import pandas as pd
from datetime import date
from pizza import Classic, Margherita, TurkPizza, PlainPizza, MixedPizza, Hawaiian, Vegetarian, MeatLovers
from decorator import Pepperoni, Sausage, Bacon, Mushrooms, Onions, Olives, PineApple, Corns

# TODO.1: Create a pizza and toppings menu.
# TODO.2: Display the menu to the customer.
# TODO.3: Ask for the pizza , size of the pizza and the toppings.
# TODO.4: If an available input is given, calculate the price according to the inputs and take an approval.
# TODO.5: After confirming, display the payment class and ask for a Name, Surname, Card Number, Card Password.
# TODO.6 : Finally, keep the user's name, user id, credit card information, description of order, time order and credit
#   card password in the "Orders_Database.csv" file, which we call the database.

pizza_types_dict = {
    "Classic": 10.99,
    "Margherita": 12.99,
    "Turkpizza": 14.99,
    "Plainpizza": 8.99,
    "Mixedpizza": 15.99,
    "Hawaiian": 13.99,
    "Vegetarian": 11.99,
    "Meatlovers": 16.99
}

toppings_dict = {
    "Pepperoni": 1.99,
    "Sausage": 2.99,
    "Bacon": 1.49,
    "Mushrooms": 0.99,
    "Onions": 0.69,
    "Olives": 1.29,
    "Pineapple": 1.49,
    "Corns": 0.99
}

pizza_price = 0
toppings_price = 0

global_pizza_chosen = ""
toppings_chosen_list = []
is_database_created = False


def pizza_selection():
    """Asks for a pizza type and calculates the chosen pizza's price(pizza_price). """
    global pizza_price, global_pizza_chosen
    for pizza_type in pizza_types_dict:
        print(f"{pizza_type}: ${pizza_types_dict[pizza_type]:.2f}")
    pizza_chosen = input("Please choose a pizza: ").title()
    global_pizza_chosen = pizza_chosen
    if pizza_chosen == "Classic":
        classic = Classic()
        classic_description = classic.get_description()
        pizza_price += classic.get_cost()
        return classic_description
    elif pizza_chosen == "Margherita":
        margherita = Margherita()
        margherita_description = margherita.get_description()
        pizza_price += margherita.get_cost()
        return margherita_description
    elif pizza_chosen == "Turkpizza":
        turkpizza = TurkPizza()
        turkpizza_description = turkpizza.get_description()
        pizza_price += turkpizza.get_cost()
        return turkpizza_description
    elif pizza_chosen == "Plainpizza":
        plainpizza = PlainPizza()
        plain_pizza_description = plainpizza.get_description()
        pizza_price += plainpizza.get_cost()
        return plain_pizza_description
    elif pizza_chosen == "Mixedpizza":
        mixedpizza = MixedPizza()
        mixedpizza_description = mixedpizza.get_description()
        pizza_price += mixedpizza.get_cost()
        return mixedpizza_description
    elif pizza_chosen == "Hawaiian":
        hawaiian = Hawaiian()
        hawaiian_description = hawaiian.get_description()
        pizza_price += hawaiian.get_cost()
        return hawaiian_description
    elif pizza_chosen == "Vegetarian":
        vegetarian = Vegetarian()
        vegetarian_description = vegetarian.get_description()
        pizza_price += vegetarian.get_cost()
        return vegetarian_description
    elif pizza_chosen == "Meatlovers":
        meatlovers = MeatLovers()
        meatlovers.get_description()
        pizza_price += meatlovers.get_cost()
        return meatlovers
    else:
        print("Please make your selection from the menu.")
        pizza_selection()


def select_topping(toppings_selected):
    """asks for toppings that will be added to pizza. Returns the desired toppings' cost. """
    if toppings_selected == "Pepperoni":
        pepperoni = Pepperoni()
        return pepperoni.get_cost()
    elif toppings_selected == "Sausage":
        sausage = Sausage()
        return sausage.get_cost()
    elif toppings_selected == "Bacon":
        bacon = Bacon()
        return bacon.get_cost()
    elif toppings_selected == "Mushrooms":
        mushrooms = Mushrooms()
        return mushrooms.get_cost()
    elif toppings_selected == "Onions":
        onions = Onions()
        return onions.get_cost()
    elif toppings_selected == "Olives":
        olives = Olives()
        return olives.get_cost()
    elif toppings_selected == "Pineapple":
        pineapples = PineApple()
        return pineapples.get_cost()
    elif toppings_selected == "Corns":
        corns = Corns()
        return corns.get_cost()


def payment():
    global is_database_created
    """Asks for name, surname, card number and card password. Creates a database order and holds the necessary infos."""
    print("In order to complete the purchasing, please fill in the followings.")
    name = input("Name: ").title()
    print(name.split())
    surname = input("Surname: ").title()
    print(surname.split())
    card_number = input("Credit Card Number: ")
    print(card_number.split())
    card_password = input("Credit Card Password: ")
    print(card_password.split())
    print("Payment done ✓")

    day = date.today()
    today = day.strftime("%d/%m/%Y")

    df = pd.DataFrame(data={
        "Name": name.split(),
        "Surname": surname.split(),
        "Card number": card_number.split(),
        "Card password": card_password.split(),
        "Day of order": today,
    })
    print(is_database_created)
    if not is_database_created:
        df.to_csv('Orders_Database.csv', index=False)
        is_database_created = True
    else:
        df.to_csv('Orders_Database.csv', index=False, mode="a", header=False)


def process():
    global toppings_price
    print("Welcome to the pizza order system!")
    print("Here are the available pizza types(All pizzas come in a 12-inch size.)")

    # Ask the user for a pizza type.
    description = pizza_selection()

    # Ask the customer for the toppings:
    is_topping_available = True
    for topping in toppings_dict:
        print(f"{topping}: ${toppings_dict[topping]:.2f}")
    while is_topping_available:
        toppings_chosen = input("Please choose toppings(Type 'exit' to move on): ").title()
        if toppings_chosen == "Exit":
            is_topping_available = False
        elif toppings_chosen in topping_list:
            toppings_price += select_topping(toppings_chosen)
            toppings_chosen_list.append(toppings_chosen)
        elif toppings_chosen not in topping_list:
            print(f"Currently out of {toppings_chosen}.")

    # Calculate the total cost of the pizza
    total_price = pizza_price + toppings_price
    print(total_price)

    # Display the order summary to the user.
    print(f"\nYour order summary: \nPizza Type: {global_pizza_chosen} (${pizza_types_dict[global_pizza_chosen]:.2f})")
    print(description)
    print("Toppings: ")
    for i in toppings_chosen_list:
        print(f"- {i}: ${toppings_dict[i]:.2f}")
    print(f"\nTotal Cost: ${total_price:.2f}")

    # Take an approval
    approval = input("Do you confirm your order('Y' or 'N'): ").upper()
    if approval == "N":
        print("We wish you a good day.")
        process()
    # Ask for order database.
    elif approval == "Y":
        payment()
        print("Thanks for choosing us. We are looking forward to see you again.")
        process()


with open("Menu.txt") as menu_file:
    menu = menu_file.readlines()
    menu_list = [pizzatype.strip() for pizzatype in menu]

with open("Toppings.txt") as toppings_file:
    toppings = toppings_file.readlines()
    topping_list = [topping.strip() for topping in toppings]

process()
