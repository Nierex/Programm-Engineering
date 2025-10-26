def reverse_lines_in_file(filename):

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines.reverse()

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Строки успешно перевёрнуты!")
