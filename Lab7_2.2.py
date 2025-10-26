import json

def add_expense():
    description = input("Описание: ")
    amount = float(input("Сумма: "))
    date = input("Дата (ДД.ММ.ГГГГ): ")
    return {"description": description, "amount": amount, "date": date}

def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)

def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_expenses(expenses):
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. [{exp['date']}] {exp['description']} — {exp['amount']} руб.")

expenses = load_expenses()

while True:
    action = input("\nВыберите действие: [1] Добавить, [2] Показать, [3] Выход: ")
    if action == '1':
        expense = add_expense()
        expenses.append(expense)
        save_expenses(expenses)
        print("Расход добавлен!")
    elif action == '2':
        show_expenses(expenses)
    elif action == '3':
        break
