def validate_card(card_number):
    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        return False, "Номер карты должен содержать только цифры!"

    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Неверная длина номера карты!"

    digits = [int(d) for d in card_number]
    checksum = 0

    for i in range(len(digits) - 1, -1, -1):
        if (len(digits) - i) % 2 == 0:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            checksum += doubled
        else:
            checksum += digits[i]

    if checksum % 10 == 0:
        return True, "Номер карты корректен!"
    else:
        return False, "Неверный номер карты!"


user_input = input("Введите номер карты: ")
is_valid, message = validate_card(user_input)
print(message)