packets = input("Введите строку из 0 и 1: ")

if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    total_packets = len(packets)
    lost_packets = packets.count('0')
    max_lost_sequence = len(max(packets.split('1'), key=len))
    loss_percent = (lost_packets / total_packets) * 100

    if loss_percent <= 1:
        quality = "отличное"
    elif loss_percent <= 5:
        quality = "хорошее"
    elif loss_percent <= 10:
        quality = "удовлетворительное"
    elif loss_percent <= 20:
        quality = "плохое"
    else:
        quality = "критическое состояние сети"

    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_lost_sequence}")
    print(f"Процент потерь: {loss_percent:.1f}%")
    print(f"Качество связи: {quality}")