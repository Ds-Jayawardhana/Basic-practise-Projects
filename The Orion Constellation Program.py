import turtle

#Set the window size
turtle.setup(500,600)
#Setup Turtle
turtle.penup()
turtle.hideturtle()


LEFT_SHOULDER_X = -100
LEFT_SHOULDER_Y = 200
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20
MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0
RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20
LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y =-140




turtle.goto(0,0)
turtle.write("Alnilum")
turtle.dot()
turtle.goto(40,20)
turtle.write("Mintaka")
turtle.dot("red")
turtle.goto(-40,-20)
turtle.write("Alnitak")
turtle.dot("red")
turtle.goto(80,180)
turtle.write("Melissa")
turtle.dot()
turtle.goto(-90,-180)
turtle.write("Saiph")
turtle.dot()
turtle.goto(120,-140)
turtle.write("Rigel")
turtle.dot()
turtle.goto(-100,200)
turtle.write("Betelgeuse")
turtle.dot()


#Drawing Lines
# Draw a line from the left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
# Draw a line from the right shoulder to right belt star
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
# Draw a line from the left belt star to middle belt star
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()
# Draw a line from the middle belt star to right belt star
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
# Draw a line from the left belt star to left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()

turtle.goto(-90,-180)
turtle.pendown()
turtle.goto(-40,-20)
turtle.penup()


turtle.goto(120,-140)
turtle.pendown()
turtle.goto(40,20)
turtle.penup()


turtle.done()