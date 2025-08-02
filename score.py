from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score=int( data.read())
        self.color("Black")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Every time you eat, I love you twice as much \nScore: {self.score}, thr high_score is : {self.high_score}",align="center",font=("Arial",15,"normal"))
    # def game_over(self):
    #     self.goto(0,0)
    #
    #     self.write( "GAME OVER!!!",align="center",font=("Arial",15,"normal"))
    def reset(self):
        if self.score >self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()
    def increase_score(self):
        self.score+=1
        self.update()
