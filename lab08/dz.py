text = input("Введите текст: ").lower()
word = input("Введите слово для поиска: ").lower()

if word in text:
    position = text.find(word)
    print(f"Слово '{word}' найдено в тексте. Позиция начала слова: {position}")
else:
    print(f"Слово '{word}' не найдено в тексте.")
