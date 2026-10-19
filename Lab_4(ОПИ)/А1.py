import random
import time

n = int(input("Введите количество примеров: "))

correct_count = 0
total_time = 0.0

for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")

    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_answer = a * b

    start_time = time.time()

    while True:
        try:
            user_answer = int(input(f"{a} x {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    time_spent = time.time() - start_time
    total_time += time_spent

    if user_answer == correct_answer:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct_count += 1
    else:
        print(f"Неверно! Правильно: {correct_answer} (Время: {time_spent:.1f} сек)")

print("=" * 40)
print("СТАТИСТИКА:")
print("=" * 40)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / n:.1f} сек")
print(f"Правильных ответов: {correct_count}/{n}")
print(f"Процент правильных: {(correct_count / n) * 100:.1f}%")