from pygame import * # Use pygame
import random

ballpic = image.load('ball.png')
ballpic.set_colorkey((0,0,0))

numBalls = 5
delay = 5

done = False

balls = []

for count in range(numBalls):
    balls.append(dict)
    balls[count] = {'x': 0,
                    'y': 0,
                    'xmove': random.randint(1, 2),
                    'ymove': random.randint(1, 2)}

init() # Start pygame
screen = display.set_mode((640, 480)) # Set Window
display.set_caption('YaBaG - Yet Another Ball Game') # Set title

event.set_grab(1)

while done == False:
    screen.fill(0) # Fill screen with black (0)
    
    for count in range(numBalls):
        screen.blit(ballpic, (balls[count]['x'], balls[count]['y'])) # Draw ball

    display.update()

    time.delay(delay) # Slow down!

    for count in range(numBalls):
        balls[count]['x'] = balls[count]['x'] + balls[count]['xmove']
        balls[count]['y'] = balls[count]['y'] + balls[count]['ymove']

        if balls[count]['x'] > 620: # Ball reached screen edges
            balls[count]['xmove'] = random.randint(-2, 0)
        if balls[count]['x'] < -10: 
            balls[count]['xmove'] = random.randint(0, 2)
        if balls[count]['y'] > 470:
            balls[count]['ymove'] = random.randint(-2, 0)
        if balls[count]['y'] < -10:
            balls[count]['ymove'] = random.randint(0, 2)

    for e in event.get(): # Check for ESC
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                done = True

    if screen.get_at((mouse.get_pos())) == (255, 255, 255, 255):
        done = True

print "You lasted for ", time.get_ticks()/1000, " seconds!"
