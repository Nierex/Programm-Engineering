def text_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    letters = sum(c.isalpha() for c in text)

    words = len(text.split())

    lines = text.count('\n') + 1

    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines} lines")
