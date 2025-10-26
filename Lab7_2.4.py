import re


def load_banned_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().strip().split()
    return set(word.lower() for word in words)


def replace_banned(text, banned_words):
    def replace_match(match):
        word = match.group(0)
        return '*' * len(word)
    pattern = '|'.join(re.escape(word) for word in banned_words)
    result = re.sub(pattern, replace_match, text, flags=re.IGNORECASE)
    return result


banned = load_banned_words('input.txt')

sentences = [
    "hello email python the exam input.txt",
    "Hello, world! Python Is the programming language of the future. My EMAIL is ....",
    "PYTHON is awesome!!!!"
]

for s in sentences:
    print(replace_banned(s, banned))
