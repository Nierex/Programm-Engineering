class InvalidInputError(Exception):

    pass

def divide_numbers(a, b):
    if b == 0:
        raise InvalidInputError("Деление на ноль запрещено")
    return a / b

def check_age(age):
    if age < 0:
        raise InvalidInputError("Возраст не может быть отрицательным")
    print(f"Возраст: {age}")

try:
    print(divide_numbers(10, 0))
except InvalidInputError as e:
    print(e)

try:
    check_age(-5)
except InvalidInputError as e:
    print(e)
