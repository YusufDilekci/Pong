import time
from turtle import Screen
from paddle_left import PaddleLeft
from paddle_right import PaddleRight
from ball import Ball
from score_board import ScoreBoard

'''
Tekrar oynamak isteyip istemeğini sor cevaba göre oyunu tekrar başlat
'''
DELAY = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

left_paddle = PaddleLeft((-350, 0))
right_paddle = PaddleRight((350, 0))
ball = Ball()
score_board = ScoreBoard()
score_board.design_screen()

game_speed = screen.textinput(title='Pong', prompt='Choose a speed of game (normal/fast/fastest) ')
if game_speed == 'fast':
    DELAY = 0.07
elif game_speed == 'fastest':
    DELAY = 0.05

screen.onkey(left_paddle.go_up, key='w')
screen.onkey(left_paddle.go_down, key='s')


screen.onkey(right_paddle.go_up, key='Up')
screen.onkey(right_paddle.go_down, key='Down')
screen.listen()


is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(DELAY) #topun hareketini bir nevi yavaşlatmış olur
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()


    #Detect collision with paddle
    if ball.distance(right_paddle) <60 and ball.xcor()> 320 or ball.distance(left_paddle) <60 and ball.xcor()< -320:
        ball.bounce_x()
        DELAY /= 1.2


    #Detect R paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        score_board.increase_score_left()
        DELAY = 0.07



    #Detect L paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        score_board.increase_score_right()
        DELAY = 0.07

        #Game over and detect who is winner
    if score_board.score_right == 10 or score_board.score_left == 10:

        if score_board.score_right == 10:
            score_board.game_over('Right')

        if score_board.score_left == 10:
            score_board.game_over('Left')

        is_game_on = False




screen.exitonclick()





