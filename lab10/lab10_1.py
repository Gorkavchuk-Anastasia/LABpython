rightCounter = 0
questionsCounter = 0
questions = ["сколько цветов у радуги? ", "какой язык мы изучаем? ", "как называется наш предмет? ", "какой сейчас месяц? ", "на каком вы курсе? "]
rightAnswers = ["7", "python", "трпо", "апрель", "3"]
while questionsCounter < len(questions):
 answer = input(questions[questionsCounter])
 if answer.lower() == rightAnswers[questionsCounter]:
    rightCounter += 1
    print("вы ответили верно")
 else:
    print("вы ответили не верно")
 questionsCounter += 1
print(f"вы набрали баллов: {rightCounter}")