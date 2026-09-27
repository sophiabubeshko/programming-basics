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