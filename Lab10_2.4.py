 class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f">>> Вызов функции: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f">>> Функция {self.func.__name__} завершена")
        return result

@MyDecorator
def greet(name):
    print(f"Привет, {name}!")

@MyDecorator
def calculate(a, b):
    return a + b

greet("Александр")
print(calculate(5, 10))
