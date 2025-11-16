import os

def read_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError("Файл не найден")
    if os.path.getsize(filename) == 0:
        raise Exception("Файл пустой")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

with open('empty.txt', 'w') as f:
    pass  

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Привет, это данные!")

try:
    read_file('empty.txt')
except Exception as e:
    print(e)

try:
    read_file('data.txt')
except Exception as e:
    print(e)
