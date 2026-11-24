text = input("Введите текст: ")
text = text.replace('!', '.')
text = text.replace('?', '.')
parts = text.split('.')
count = 0

for part in parts:
    clean_part = part.strip()
    if clean_part != "":
        print(clean_part)
        count = count + 1

print("Предложений в тексте:", count)