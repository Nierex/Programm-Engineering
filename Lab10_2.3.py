 def add_two():
    try:
        user_input = input("Введите число: ")
        number = int(user_input)
        result = 2 + number
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидаемо число.")

add_two()
