counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Третий вопрос
answer = input("В какой группе вы учитесь?\n")
if answer == "П-21" or answer == "п-21":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
 #Четвертый вопрос
answer = input("На каком вы курсе?\n")
if answer == "3":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
print(f"вы набрали баллов {counter}")
