studentList = ["Вася", "Петя"]
while True:
    answer = int(input("выберите действие\n"
                    "1-добавить студента\n"
                    "2-удалить студента\n"
                    "3-посмотреть весь список студентов\n"
                    "0-выйти из программы\n"))
    if answer not in [1, 2 ,3, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента ")
        studentList.append(newStudent)
    elif answer == 2:
        delNumber = input("введите имя студента для удаления ")
        studentList.remove(delNumber)
    elif answer == 3:
        print(studentList)
    elif answer == 0:
        break