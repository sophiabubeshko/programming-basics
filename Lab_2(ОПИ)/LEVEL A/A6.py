# --- Задание А6 ---
print("\n--- Задание А6 ---")
N = int(input("Введите секунды: "))

hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60

print("{}:{:02}:{:02}".format(hours, minutes, seconds))