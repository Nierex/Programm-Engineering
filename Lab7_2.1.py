 from collections import Counter
import re
def find_most_common_word(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
   words = re.findall(r'[a-zA-Z]+', text)
    word_count = Counter(words)
    most_common = word_count.most_common(1)[0]
    print(f"Всего слов: {len(words)}")
    print(f"Самое частое слово: '{most_common[0]}' — встречается {most_common[1]} раз")

