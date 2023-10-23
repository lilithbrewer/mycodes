import turtle
# make drawing pallet
wn = turtle.screen()
wn.title("Pong")
wn.setup(width=800, height=600)
wn.bigcolor("black")
wn.tracer(0) 

# define paddle A
paddle_b = turtle.turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.speed(10)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350.0)

# 
while True:
    wn.update()


