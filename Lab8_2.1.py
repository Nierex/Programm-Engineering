  class CoffeeMachine:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity

    def brew_coffee(self):
        return f"Молоть кофе на {self.brand} с ёмкостью {self.capacity} мл"

machine = CoffeeMachine("Bosch", 1500)
print(machine.brew_coffee())
