import turtle
# первая звездочка
turtle.shape("turtle")
turtle.speed(5)
turtle.left(100)
turtle.color("blue","green")
turtle.width(5)
for i in range(4):
    for i in range(5):
        turtle.left(144)
        turtle.forward(150)
# второая звездочка
# #Подымаем перо
    turtle.penup()
    turtle.forward(250)

#Опускаем перо
    turtle.pendown()
    turtle.color("pink","red")
    turtle.width(3)
    for i in range(9):
        turtle.left(160)
        turtle.forward(150)
    turtle.penup()
    turtle.left(90)
    turtle.forward(250)
    turtle.pendown()
    turtle.color("blue","green")
    turtle.width(5)




turtle.exitonclick()
