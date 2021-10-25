# Date created: Thu Oct 21 15:34:26 2021
# Last date modified: Sat Jul 24 17:17:04 2021
import turtle
turtle.shape('turtle')

numbers = [1,2,3]
i = 0
while(i < len(numbers)):
    if (numbers[i] + 2) < 20:
        turtle.goto(-685,0)
        turtle.speed(1)
        turtle.forward(100)

