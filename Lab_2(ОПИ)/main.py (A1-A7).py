
# ==========================================
# Практическая работа 2. Уровень А (Базовый)
# ==========================================

# --- Задание А1 ---
print("--- Задание А1 ---")
width = 17
height = 12.0

print("1.", width // 2, type(width // 2))
print("2.", width / 2.0, type(width / 2.0))
print("3.", height / 3, type(height / 3))
print("4.", 1 + 2 * 5, type(1 + 2 * 5))


# --- Задание А2 ---
print("\n--- Задание А2 ---")
# Здесь просто выводим текстом результаты проверок, которые ты делала в терминале
print("1. '123e' - нельзя, ошибка ValueError")
print("2. '91.4' - нельзя, ошибка ValueError")
print("3. 524.345 ** 435345345311145345 - нельзя, OverflowError")
print("4. '7.1 + 4' - нельзя, ошибка ValueError")
print("5. '4' - 2 - нельзя, ошибка TypeError")
print("6. '4 - 2' - нельзя, ошибка ValueError")
print("7. '42' - можно, результат 42")
print("8. -12.12 - можно, результат -12")


# --- Задание А3 ---
print("\n--- Задание А3 ---")
bayty = 1921000
megabayty = bayty / 1024 / 1024
print("Размер в мегабайтах:", megabayty)


# --- Задание А4 ---
print("\n--- Задание А4 ---")
A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A > B:
    print(A)
else:
    print(B)


# --- Задание А5 ---
print("\n--- Задание А5 ---")
A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A % B == 0:
    print("YES")
else:
    print("NO")


# --- Задание А6 ---
print("\n--- Задание А6 ---")
N = int(input("Введите секунды: "))

hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60

print("{}:{:02}:{:02}".format(hours, minutes, seconds))


# --- Задание А7 ---
print("\n--- Задание А7 ---")
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

sum1 = x1 + y1
sum2 = x2 + y2

if sum1 % 2 == sum2 % 2:
    print("YES")
    if sum1 % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")
