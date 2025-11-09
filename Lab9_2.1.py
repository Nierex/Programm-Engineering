 class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print(f"{self.name} работает...")
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
        else:
            print("Урожай ещё не созрел! Продолжайте ухаживать.")
    @staticmethod
    def knowledge_base():
        print("""
        Справка по садоводству:
- Помидор проходит 4 стадии: отсутствует → цветение → зеленый → красный.
- Когда все помидоры красные — можно собирать урожай.
- Если собирать раньше — урожай будет неполным.
""")


# ТЕСТЫ
#1
Gardener.knowledge_base()
#2
bush = TomatoBush(5)
gardener = Gardener("Анна", bush)
#3
print("\n--- Уход за кустом ---")
gardener.work()  # 1-й день
gardener.work()  # 2-й день
gardener.work()  # 3-й день
#4
gardener.harvest()
#5
gardener.work()  # 4-й день
gardener.harvest()

print(f"Количество помидоров на кусте после сбора: {len(bush.tomatoes)}")
