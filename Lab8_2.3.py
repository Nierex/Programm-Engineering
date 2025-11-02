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

class SmartCoffeeMachine(CoffeeMachine):
    def __init__(self, brand, capacity, wifi_enabled=True):
        super().__init__(brand, capacity)
        self.wifi_enabled = wifi_enabled
    def brew_coffee_remotely(self):
        if not self.wifi_enabled:
            return "Wi-Fi выключен. Невозможно приготовить кофе удалённо."
        return f"Удалённое приготовление кофе на {self.brand} через Wi-Fi"
smart_machine = SmartCoffeeMachine("Nespresso", 1200, True)
print(smart_machine.brew_coffee_remotely())
print(smart_machine.brew_coffee())
