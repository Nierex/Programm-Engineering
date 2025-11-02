class Beverage:
    def prepare(self):
        pass
class Tea(Beverage):
    def prepare(self):
        return "Завариваем чай..."
class Coffee(Beverage):
    def prepare(self):
        return "Готовим кофе..."
class Smoothie(Beverage):
    def prepare(self):
        return "Блендируем смузи..."
beverages = [Tea(), Coffee(), Smoothie()]
for drink in beverages:
    print(drink.prepare())
