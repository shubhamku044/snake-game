from turtle import Turtle
POSITIONS = [(0,0), (-20 ,0)]
MOVE = 20

UP = 90 
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    
    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)


    def add_segment(self, position):
        seg = Turtle(shape = "square")
        seg.color("white")
        seg.penup()
        seg.speed(2)
        seg.goto(position)
        self.segment.append(seg)




    def extend(self):
        self.add_segment(self.segment[-1].position())




    def move(self):
        for seg_num in range(len(self.segment)-1, 0 , -1):
            x = self.segment[seg_num-1].xcor()
            y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(x , y)
        self.segment[0].forward(MOVE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
