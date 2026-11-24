text = input("Введите текст: ")
words = text.split()
result = ""

for word in words:
    if len(word) >= 3:
        first_letter = word[0].upper()
        result = result + first_letter

print(result)