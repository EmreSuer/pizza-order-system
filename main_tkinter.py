from tkinter import *
from pizza import Classic, Margherita, TurkPizza, PlainPizza, MixedPizza, Hawaiian, Vegetarian, MeatLovers
from decorator import Pepperoni, Sausage, Bacon, Mushrooms, Onions, Olives, PineApple, Corns
import datetime
import pandas as pd

COLOR = "#f7f5dd"
MENU_COLOR = "#fe2400"
total_cost = 0
toppings_cost = 0
info_label = ""
entry_name = ""
entry_surname = ""
entry_card_ID = ""
entry_card_password = ""
submit_button = None
is_database_created = False
is_order_created = False
order_text = ""


def order():
    """Prints the order according to the choices made."""
    global toppings_cost, is_order_created, order_text, total_cost
    if not is_order_created:
        order_text = "You ordered a {} {} pizza with toppings of".format(size_var.get().split(",")[0], type_var.get().split(",")[1])
        if mushrooms_var.get():
            order_text += " ,mushrooms"
            toppings_cost += Mushrooms().get_cost()
        if olives_var.get():
            order_text += " ,olives"
            toppings_cost += Olives().get_cost()
        if onions_var.get():
            order_text += " ,onions"
            toppings_cost += Onions().get_cost()
        if pepperoni_var.get():
            order_text += " ,pepperoni"
            toppings_cost += Pepperoni().get_cost()
        if bacon_var.get():
            order_text += " ,bacon"
            toppings_cost += Bacon().get_cost()
        if corns_var.get():
            order_text += " ,corns"
            toppings_cost += Corns().get_cost()
        if sausage_var.get():
            order_text += " ,sausage"
            toppings_cost += Sausage().get_cost()
        if pineapple_var.get():
            order_text += " ,pineapple"
            toppings_cost += PineApple().get_cost()
        order_text += ""
        order_label.config(text=order_text)

        total_cost = round((float(type_var.get().split(',')[0]) + toppings_cost) * float(size_var.get().split(",")[1]), 2)

        cost_text = f"Total cost: {total_cost}"
        cost_label.config(text=cost_text)
        is_order_created = True
    else:
        order_text = ""
        order_label.config(text="")
        total_cost = 0
        toppings_cost = 0
        cost_label.config(text="")
        is_order_created = False
        order()


def checkbutton_used():
    """ Prints 1 if Approve button checked, otherwise 0."""
    global info_label, entry_name, entry_surname, entry_card_ID, entry_card_password, submit_button

    def temp_entry_name(event):
        """Makes the entry widget temporary."""
        entry_name.delete(0, "end")

    def temp_entry_surname(event):
        entry_surname.delete(0, "end")

    def temp_entry_id(event):
        entry_card_ID.delete(0, "end")

    def temp_entry_password(event):
        entry_card_password.delete(0, "end")

    def submit():
        """Gets the info written into the textbox when it is clicked."""
        global is_database_created, is_order_created
        if is_order_created:
            now = datetime.datetime.now()
            day_time = now.strftime("%d-%m-%Y %H:%M:%S")

            output_label = Label(text=f"{entry_name.get()} {entry_surname.get()}, {day_time}", bg=COLOR)
            output_label.place(x=420, y=540)

            completed_label = Label(text=" Payment is Done ✓ ", bg=COLOR)
            completed_label.place(x=420, y=580)

            # Create a order database
            df = pd.DataFrame(data={
                "Name": entry_name.get().split(),
                "Surname": entry_surname.get().split(),
                "Card number": entry_card_ID.get().split(),
                "Card password": entry_card_password.get().split(),
                "Day of order": day_time,
            })
            print(is_database_created)
            if not is_database_created:
                df.to_csv('Orders_Database.csv', index=False)
                is_database_created = True
            else:
                df.to_csv('Orders_Database.csv', index=False, mode="a", header=False)

    if checked_state.get() == 1:
        info_label = Label(text="Please fill in the followings correctly to complete the payment.", bg=COLOR)
        info_label.place(x=70, y=500)

        # Create an entry in order to take the order payment
        entry_name = Entry(width=50, bg=COLOR)
        entry_name.insert(0, string="Enter your name...".title())
        entry_name.place(x=80, y=520)
        entry_name.bind("<FocusIn>", temp_entry_name)

        entry_surname = Entry(width=50, bg=COLOR)
        entry_surname.insert(0, string="Enter your surname...".title())
        entry_surname.place(x=80, y=540)
        entry_surname.bind("<FocusIn>", temp_entry_surname)

        entry_card_ID = Entry(width=50, bg=COLOR)
        entry_card_ID.insert(0, string="Enter your card Number...")
        entry_card_ID.place(x=80, y=560)
        entry_card_ID.bind("<FocusIn>", temp_entry_id)

        entry_card_password = Entry(width=50, bg=COLOR)
        entry_card_password.insert(0, string="Enter your card password...")
        entry_card_password.place(x=80, y=580)
        entry_card_password.bind("<FocusIn>", temp_entry_password)

        # Button for submitting the payment info.
        submit_button = Button(text="Submit", bg=COLOR, command=submit)
        submit_button.place(x=200, y=600)
    else:
        info_label.config(text=" ")
        entry_name.destroy()
        entry_surname.destroy()
        entry_card_ID.destroy()
        entry_card_password.destroy()
        submit_button.destroy()


def get_radiobutton_value():
    """returns the chosen pizza type's cost."""
    type_var.get()


# Create a window
window = Tk()
window.title("PizzaOrderSystem")
window.minsize(width=750, height=650)
window.config(padx=20, pady=20, bg=COLOR)

# Create a canvas for the pizza background image.
canvas = Canvas(width=230, height=219, bg=COLOR, highlightthickness=0)
pizza_image = PhotoImage(file="pizza_image.png")
canvas.create_image(115, 109, image=pizza_image)
canvas.place(x=450, y=190)

# Create the labels
menu_label = Label(window, text="MENU", bg=COLOR, font=("Courier", 36, "italic"), fg=MENU_COLOR)
menu_label.place(x=10, y=0)

size_label = Label(window, text="Size:", bg=COLOR)
size_label.place(x=170, y=210)

type_label = Label(window, text="Type:", bg=COLOR)
type_label.place(x=0, y=210)

toppings_label = Label(window, text="Toppings:", bg=COLOR)
toppings_label.place(x=300, y=210)

# Create the radio buttons for pizza type
type_var = StringVar()
type_var.set(" ")

classic_radio = Radiobutton(text=f"Classic: {Classic().get_cost()} ", variable=type_var, value=f"{Classic().get_cost()},Classic", bg=COLOR, command=get_radiobutton_value)
classic_radio.place(x=0, y=230)

margherita_radio = Radiobutton(text=f"Margherita: {Margherita().get_cost()}", variable=type_var, value=f"{Margherita().get_cost()},Margherita", bg=COLOR, command=get_radiobutton_value)
margherita_radio.place(x=0, y=250)

turkpizza_radio = Radiobutton(text=f"Turkpizza: {TurkPizza().get_cost()}", variable=type_var, value=f"{TurkPizza().get_cost()},Turkpizza", bg=COLOR, command=get_radiobutton_value)
turkpizza_radio.place(x=0, y=270)

plainpizza_radio = Radiobutton(text=f"Plainpizza: {PlainPizza().get_cost()}", variable=type_var, value=f"{PlainPizza().get_cost()},Plainpizza", bg=COLOR, command=get_radiobutton_value)
plainpizza_radio.place(x=0, y=290)

mixedpizza_radio = Radiobutton(text=f"Mixedpizza: {MixedPizza().get_cost()}", variable=type_var, value=f"{MixedPizza().get_cost()},Mixedpizza", bg=COLOR, command=get_radiobutton_value)
mixedpizza_radio.place(x=0, y=310)

hawaiian_radio = Radiobutton(text=f"Hawaiian: {Hawaiian().get_cost()}", variable=type_var, value=f"{Hawaiian().get_cost()},Hawaiian", bg=COLOR, command=get_radiobutton_value)
hawaiian_radio.place(x=0, y=330)

vegetarian_radio = Radiobutton(text=f"Vegetarian: {Vegetarian().get_cost()}", variable=type_var, value=f"{Vegetarian().get_cost()},Vegetarian", bg=COLOR, command=get_radiobutton_value)
vegetarian_radio.place(x=0, y=350)

meatlovers_radio = Radiobutton(text=f"Meatlovers: {MeatLovers().get_cost()}", variable=type_var, value=f"{MeatLovers().get_cost()},Meatlovers", bg=COLOR, command=get_radiobutton_value)
meatlovers_radio.place(x=0, y=370)

# Create the radio buttons for pizza size
size_var = StringVar()
size_var.set(" ")

small_radio = Radiobutton(window, text="Small", variable=size_var, value="Small,1", bg=COLOR)
small_radio.place(x=170, y=230)

medium_radio = Radiobutton(window, text="Medium", variable=size_var, value="Medium,1.5", bg=COLOR)
medium_radio.place(x=170, y=250)

large_radio = Radiobutton(window, text="Large", variable=size_var, value="Large,2", bg=COLOR)
large_radio.place(x=170, y=270)


# Create the checkboxes for toppings
pepperoni_var = IntVar()
pepperoni_checkbox = Checkbutton(window, text=f"Pepperoni: {Pepperoni().get_cost()}", variable=pepperoni_var, bg=COLOR)
pepperoni_checkbox.place(x=300, y=230)

sausage_var = IntVar()
sausage_checkbox = Checkbutton(window, text=f"Sausage: {Sausage().get_cost()}", variable=sausage_var, bg=COLOR)
sausage_checkbox.place(x=300, y=250)

bacon_var = IntVar()
bacon_checkbox = Checkbutton(window, text=f"Bacon: {Bacon().get_cost()}", variable=bacon_var, bg=COLOR)
bacon_checkbox.place(x=300, y=270)

mushrooms_var = IntVar()
mushrooms_checkbox = Checkbutton(window, text=f"Mushrooms: {Mushrooms().get_cost()}", variable=mushrooms_var, bg=COLOR)
mushrooms_checkbox.place(x=300, y=290)

onions_var = IntVar()
onions_checkbox = Checkbutton(window, text=f"Onions: {Onions().get_cost()}", variable=onions_var, bg=COLOR)
onions_checkbox.place(x=300, y=310)

olives_var = IntVar()
olives_checkbox = Checkbutton(window, text=f"Olives: {Olives().get_cost()}", variable=olives_var, bg=COLOR)
olives_checkbox.place(x=300, y=330)

pineapple_var = IntVar()
pineapple_checkbox = Checkbutton(window, text=f"Pineapple: {PineApple().get_cost()}", variable=pineapple_var, bg=COLOR)
pineapple_checkbox.place(x=300, y=350)

corns_var = IntVar()
corns_checkbox = Checkbutton(window, text=f"Corns: {Corns().get_cost()}", variable=corns_var, bg=COLOR)
corns_checkbox.place(x=300, y=370)


# Create order button to give a display of order.
order_button = Button(window, text="Order", command=order, bg=COLOR)
order_button.place(x=180, y=380)


order_label = Label(window, text="", bg=COLOR)
order_label.place(x=10, y=420)

cost_label = Label(window, text="", bg=COLOR)
cost_label.place(x=160, y=440)


# Listbox
listbox = Listbox(height=8, width=110, bg=COLOR)
pizzas = [f"Classic: {Classic().get_description()}",
          f"Margherita: {Margherita().get_description()}",
          f"Turkpizza: {TurkPizza().get_description()}",
          f"Plainpizza: {PlainPizza().get_description()}",
          f"Mixedpizza: {MixedPizza().get_description()}.",
          f"Hawaiian: {Hawaiian().get_description()}",
          f"Vegetarian: {Vegetarian().get_description()}",
          f"Meatlovers: {MeatLovers().get_description()}"
          ]
for item in pizzas:
    listbox.insert(pizzas.index(item), item)
listbox.place(x=10, y=60)

# Checkbutton for approval.
checked_state = IntVar()
checkbutton = Checkbutton(text="Do you confirm your order?", variable=checked_state, command=checkbutton_used, bg=COLOR)
checked_state.get()
checkbutton.place(x=120, y=470)


window.mainloop()
