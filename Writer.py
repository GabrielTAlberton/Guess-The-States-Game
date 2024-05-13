from turtle import Turtle

FONT = ("Courier", 6, "normal")

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def walk_to_state(self, x, y):
        self.goto(x, y)
        # self.write(f"{loop_state}", align="center", font=FONT )

    def write_state_name(self, state_name):
        self.write(f"{state_name}", align="center", font=FONT)




