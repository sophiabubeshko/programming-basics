print("ПРЯМОУГОЛЬНИК 5x10:")
for i in range(5):
    for j in range(10):
        print("#", end="")
    print()

print()

print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(1, 6):
    for j in range(i):
        print("#", end="")
    print()

print()

rows = 5
cols = 10
print(f"РАМКА {rows}x{cols}:")
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()