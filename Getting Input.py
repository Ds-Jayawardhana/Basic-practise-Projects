import turtle
radius=turtle.numinput("Input a value","Enter value for the radius",default=80,minval=50,maxval=250)
color=turtle.textinput("Input a Color","Enter Color for the circle")
turtle.pencolor(color)
turtle.bgcolor("black")
turtle.fillcolor(color)
turtle.begin_fill()
turtle.circle(radius)
turtle.speed(1)
turtle.end_fill()
turtle.done()# To keep the graphic window to open