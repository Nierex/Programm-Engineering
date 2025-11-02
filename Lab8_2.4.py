class CoffeeMachine:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.water_level = 0

    class CoffeeMachine:
        def __init__(self, brand, capacity):
            self._brand = brand 
            self.__capacity = capacity
        def get_capacity(self):
            return self.__capacity
        def set_capacity(self, new_capacity):
            if new_capacity > 0:
                self.__capacity = new_capacity
            else:
                print("Ёмкость должна быть положительной!")
        def brew_coffee(self):
            return f"Молоть кофе на {self._brand} с ёмкостью {self.__capacity} мл"
    machine = CoffeeMachine("Delonghi", 1000)
    print(machine.brew_coffee())
    print(machine.get_capacity())
    machine.set_capacity(1500)
    print(machine.get_capacity())
