import random

while True:
    answer = input("Задайте вопрос: \n").lower()
    bot = random.choice(["да","нет","может быть"])
    print(f"{bot}")
    next = input("Хотите попробовать еще раз? ")
    if next.lower() != "да":
        break
print(f"Попробуйте еще!")    