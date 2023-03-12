class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Classic(Pizza):
    def __init__(self):
        super().__init__(cost=10.99, description="Tomato sauce, mozzarella cheese, pepperoni, sausage, mushrooms, "
                                                 "and olives.")


class Margherita(Pizza):
    def __init__(self):
        super().__init__(cost=12.99, description="A classic pizza with tomato sauce, mozzarella and cheese, for a "
                                                 "simple yet delicious taste.")


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__(cost=14.99, description="A spicy pizza with tomato sauce, mozzarella cheese and ground beef, "
                                                 "for a bold and flavorful taste.")


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__(cost=8.99, description="A simple yet delicious pizza with tomato sauce and mozzarella cheese.")


class MixedPizza(Pizza):
    def __init__(self):
        super().__init__(cost=15.99, description="A loaded pizza with tomato sauce, mozzarella cheese, pepperoni, "
                                                 "sausage and onions for a satisfying meal")


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__(cost=13.99, description="A tropical twist on the classic pizza with tomato sauce, mozzarella "
                                                 "cheese and pineapple for a sweet flavor.")


class Vegetarian(Pizza):
    def __init__(self):
        super().__init__(cost=11.99,
                         description="A flavorful pizza with tomato sauce, mozzarella cheese, "
                                     "onions and olives for a fresh and healthy option. ")


class MeatLovers(Pizza):
    def __init__(self):
        super().__init__(cost=16.99, description="A hearty pizza with tomato sauce, mozzarella cheese, pepperoni, "
                                                 "sausage and bacon for the ultimate indulgence.")
