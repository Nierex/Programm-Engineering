import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Имя каталога {catalog[0]} содержит:')
        print(f'Подкаталоги: {", ".join(folder for folder in catalog[1])}')
        print(f'Файлы: {", ".join(file for file in catalog[2])}')
        print('-' * 40)

print_docs('C:\\Users\\Александр\\Pictures')
