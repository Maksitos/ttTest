import os
import time
import pynput
from pynput.keyboard import Key


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


def moveBall():
    global ball_y, ball_x, directionBall_y, directionBall_x
    if ball_y == height - 1 or ball_y == 1 :
        directionBall_y *= -1
    ball_y += directionBall_y
    if (rocket1 <= ball_y < rocket1 + rocketLength and ball_x == 1) \
            or (rocket2 <= ball_y < rocket2 + rocketLength and ball_x == width - 1) :
        directionBall_x *= -1
    elif ball_x <= 0:
        exit('Player 2 Win!')
    elif ball_x >= width:
        exit('Player 1 Win!')
    ball_x += directionBall_x

def on_press(key):
    global rocket2, rocket1, rocketLength
    if key == Key.up:
        if 1 <= rocket2:
            rocket2 -= 1
    if key == Key.down:
        if rocket2 <= height - rocketLength:
            rocket2 += 1
    if key == pynput.keyboard.KeyCode.from_char('w'):
        if 1 <= rocket1:
            rocket1 -= 1
    if key == pynput.keyboard.KeyCode.from_char('s'):
        if rocket1 <= height - rocketLength:
            rocket1 += 1


def on_release(key):
    pass
    # print(key)


pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()


while True:
    draw()
    moveBall()
    time.sleep(0.1)
    os.system('cls')

