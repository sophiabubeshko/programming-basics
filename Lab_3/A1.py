# Задание A1
print("Введите координаты первой точки (x1, y1):")
x1 = int(input())
y1 = int(input())

print("Введите координаты второй точки (x2, y2):")
x2 = int(input())
y2 = int(input())

# Проверяем каждую четверть
if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("Yes, I")
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("Yes, II")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("Yes, III")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("Yes, IV")
else:
    print("No")