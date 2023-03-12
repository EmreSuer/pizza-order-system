class Decorator:
    def __init__(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost


class Pepperoni(Decorator):
    def __init__(self):
        super().__init__(cost=1.99)


class Sausage(Decorator):
    def __init__(self):
        super().__init__(cost=2.99)


class Bacon(Decorator):
    def __init__(self):
        super().__init__(cost=1.49)


class PineApple(Decorator):
    def __init__(self):
        super().__init__(cost=1.49)


class Olives(Decorator):
    def __init__(self):
        super().__init__(cost=1.29)


class Mushrooms(Decorator):
    def __init__(self):
        super().__init__(cost=0.99)


class Onions(Decorator):
    def __init__(self):
        super().__init__(cost=0.69)


class Corns(Decorator):
    def __init__(self):
        super().__init__(cost=0.99)
