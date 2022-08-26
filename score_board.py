from turtle import Turtle

ALIGNMENT_SCORE = 'center'
FONT_SCORE = ('Courier', 80, 'normal')
ALIGNMENT_WINNER = 'center'
FONT_WINNER = ('Arial', 40, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.update_score()


    def update_score(self):
        self.write(f' {self.score_left}  {self.score_right} ', False, ALIGNMENT_SCORE, font=FONT_SCORE)


    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_score()

    def game_over(self, who_win):
        self.color('brown')
        self.home()
        self.write(f'{who_win} side is winner',  False, ALIGNMENT_WINNER, font=FONT_WINNER)

    def design_screen(self):
        new_y = 280
        for count in range(1, 10):
            design = Turtle('square')
            design.shapesize(stretch_wid=1, stretch_len=0.3)
            design.color('blue')
            design.penup()
            design.goto(0, new_y)
            new_y -= 65