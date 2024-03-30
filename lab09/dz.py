studentMark = [5, 3]
studentList = ["Вася","Петя"]
while True:
    answer = int(input("выберите действие\n"
                    "1-добавить студента\n"
                    "2-удалить студента\n"
                    "3-посмотреть весь список студентов\n"
                    "0-выйти из программы\n"))
    if answer not in [1, 2 ,3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента ")
        studentList.append(newStudent)
        newMark = int(input("Введите оценку для студента: "))
        studentMark.append(newMark)
    elif answer == 2:
        delNumber = input("введите имя студента для удаления ")
        studentList.remove(delNumber)
    elif answer == 3:
        dlina = len(studentList)
        for i in range(dlina):
            print(f"{studentList[i]} {studentMark[i]}")
    elif answer == 0:
        break