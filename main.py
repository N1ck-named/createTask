import pygame # this import, known as pygame, allows for visual code and game development. This import is made by Pete Shinners found at: https://www.pygame.org/docs/
from playsound import playsound # this module, known as playsound, allows for sounds from mp3 files to play during a program. This module is maintained by aylorSMarks and is found at: https://pypi.org/project/playsound/
import random

# starts the screen
print("|-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-|")
pygame.init()
screen = pygame.display.set_mode()
sw, sh = screen.get_size()
screen = pygame.display.set_mode((sw, sw*(9/16)))
sw, sh = screen.get_size()

# start variables & pygame functions
running = True
clock = pygame.time.Clock()
fr = 0 # frame rate for game
clicks = [120, 30] # var 1 = how many clicks, var 2-beyond = what click will the met play

# running code 
while running:
    screen.fill((150, 150, 150))
    pygame.display.flip()

    clock.tick(60)  # limits frame rate, 30 clicks ~= 0.75 seconds
    fr += 1
    if fr % clicks[1] == 0:
        playsound("C:\\Users\\kip\\Programing stuff\\Random code files python\\createTask\\Met.mp3", False) # "put raw path of mp3 file"
        if fr == clicks[0]:
            fr = 0

    # key binds and actions
    for event in pygame.event.get():

        keys=pygame.key.get_pressed()
        
        # note keys
        if keys[pygame.K_r]:
            playsound("C:\\Users\\kip\\Programing stuff\\Random code files python\\createTask\\Placeholder.mp3", False)
            print("r")
        if keys[pygame.K_l]:
            playsound("C:\\Users\\kip\\Programing stuff\\Random code files python\\createTask\\Placeholder.mp3", False)
            print("l")
        # quit
        if keys[pygame.K_ESCAPE]:

            print("|-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-|")
            running = False