import turtle
import time
def gambar_hati():
    window = turtle.Screen()
    window.bgcolor("pink")
    window.title("Hati Untukmu")
    
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(5)
    pen.pensize(3)
    pen.color("red")
    
    # Gambar hati
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.setheading(60)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()
    
    # Tulis pesan
    pen.penup()
    pen.goto(0, 50)
    pen.color("white")
    pen.write("I <3 You!", align="center", font=("Arial", 24, "bold"))
    
    pen.goto(0, 0)
    pen.write("Kamu adalah alasan aku tersenyum", align="center", font=("Arial", 16, "normal"))
    
    time.sleep(5)

gambar_hati()