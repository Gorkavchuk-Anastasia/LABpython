import random

timeList = "Сегодня", "Завтра", "Очень скоро"
eventList = "вы встретите", "с вами случится", "вы найдёте"
objectList = "что-то волшебное", "необычный инцидент", "большой сюрприз"
correct = ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]

while True:
    zodiac = input("Введите знак Зодиака: ")
    if zodiac.lower() not in correct:
        print("Пожалуйста, введите корректный знак Зодиака.")
        continue

    time = timeList[random.randint(0, len(timeList) - 1)]
    event = eventList[random.randint(0, len(eventList) - 1)]
    object = objectList[random.randint(0, len(objectList) - 1)]

    print(time + " " + event + " " + object)

    next = input("Хотите попробовать ещё раз? (да/нет): ")
    if next.lower() != "да":
        break
print("Приходите ещё за новыми предсказаниями!")