text = input("Введите текст: ")
result = text

while '(' in result:
    start = result.find('(')
    end = result.find(')')

    if end != -1:
        result = result[:start] + result[end + 1:]
    else:
        break

print("Исходный текст:", text)
print("Укороченный текст:", result.strip())