import random
print("Добро пожаловать в игру 'Камень, ножницы, бумага, ящерица, Спок'!")

rounds = int(input("Введите количество раундов: "))
playerScore = 0
botScore = 0

for i in range(rounds):
    print(f"\nРаунд {i + 1}:")
    print("Камень - 1")
    print("Ножницы - 2")
    print("Бумага - 3")
    print("Ящерица - 4")
    print("Спок - 5")
    
    answer = input("Что выберешь?\n").lower()
    if answer.find("1") != -1:
        answer = "к"
    elif answer.find("2") != -1:
        answer = "н"
    elif answer.find("3") != -1:
        answer = "б"
    elif answer.find("4") != -1:
        answer = "я"
    elif answer.find("5") != -1 or answer.find("5") != -1:
        answer = "с"
    
    botAnswer = random.choice(["камень", "ножницы", "бумага", "ящерица", "спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    
    if answer == botAnswer:
        print("Ничья!")
    elif (answer == "к" and botAnswer == "н") or \
         (answer == "н" and botAnswer == "б") or \
         (answer == "б" and botAnswer == "к") or \
         (answer == "с" and botAnswer == "к") or \
         (answer == "с" and botAnswer == "н") or \
         (answer == "б" and botAnswer == "с") or \
         (answer == "я" and botAnswer == "б") or \
         (answer == "б" and botAnswer == "я") or \
         (answer == "к" and botAnswer == "я") or \
         (answer == "н" and botAnswer == "я"):
        print("Ты победил!")
        playerScore += 1
    else:
        print("Я победил!")
        botScore += 1
    
    print(f"Счет: Игрок {playerScore} : {botScore} Бот")

if playerScore == botScore:
    print("\nНичья по итогам всех раундов!")
elif playerScore > botScore:
    print("\nТы победил по итогам всех раундов!")
else:
    print("\nЯ победил по итогам всех раундов!")
