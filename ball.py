from pygame import * # Use pygame

ballpic = image.load('ball.png')

done = False

ballX = 0
ballY = 0 # Ball position

ballXMove = 1
ballYMove = 1

init() # Start pygame
screen = display.set_mode((640, 480)) # Set Window
display.set_caption('YaBaG - Yet Another Ball Game') # Set title

while done == False:
    screen.fill(0) # Fill screen with black (0)
    screen.blit(ballpic, (ballX, ballY)) # Draw ball
    display.update()

    time.delay(5) # Slow down!

    ballX = ballX + ballXMove
    ballY = ballY + ballYMove # Update ball position

    if ballX > 600: # Ball reached screen edges
        ballXMove = -1
    if ballX < 0:
        ballXMove = 1
    if ballY > 440:
        ballYMove = -1
    if ballY < 0:
        ballYMove = 1

    for e in event.get(): # Check for ESC
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                done = True
