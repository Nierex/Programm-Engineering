class CoffeeMachine:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.water_level = 0  
    def brew_coffee(self):
        if self.water_level < 200:
            return "Недостаточно воды!"
        self.water_level -= 200
        return f"Кофе приготовлен на {self.brand}"
    def refill_water(self, amount):
        self.water_level += amount
        return f"Добавлено {amount} мл воды. Текущий уровень: {self.water_level} мл"
machine = CoffeeMachine("Bosch", 1500)
machine.refill_water(500)
print(machine.brew_coffee())
print(machine.brew_coffee())
print(machine.brew_coffee())
