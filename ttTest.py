import os
import time

width = 50
height = 20
ball_x = 15
ball_y = 10

rocket1 = 11
rocket2 = 8
rocketLength = 3

directionBall_x = 1
directionBall_y = -1


def draw():
    height_p = 0
    while height_p <= height:
        width_p = 0
        result = ''
        while width_p <= width:
            if ball_y == height_p and width_p == ball_x:
                result += 'o'
            elif width_p == 0 and rocket1 <= height_p < rocket1 + rocketLength:
                result += ']'
            elif width_p == width and rocket2 <= height_p < rocket2 + rocketLength:
                result += '['
            elif height_p == 0:
                result += 'i'
            elif height_p == height:
                result += 'i'
            else:
                result += ' '
            width_p += 1
        print(result)
        height_p += 1

    pass


def moveBall():
    pass

while True:
    draw()
    time.sleep(0.1)
    os.system('cls')

