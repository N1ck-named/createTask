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
keyDowns = [False,False] # [right hand, left hand]
start = False
listen = True
fadingTextEffect = []

# functions
startFont = pygame.font.SysFont("Adobe Gothic Std Kalin", sw//8) # learned to add text from this video (lines 21-23,25): https://www.youtube.com/watch?v=ndtFoWWBAoE&t=84s
gameFont = pygame.font.SysFont("Adobe Gothic Std Kalin", sw//20)
def addText(txt, txtFont, color, x, y, transparent=255): # note, text x and y is set to go to top left corner, not the center
    image = txtFont.render(txt,True,color)
    image.set_alpha(transparent) # learned how to set transpenency from this stack overflow thread: https://stackoverflow.com/questions/6339057/draw-transparent-rectangles-and-polygons-in-pygame
    screen.blit(image, (x,y))
    return [txt, color, x+sw//100, y+sw//100, transparent - transparent//10]

# running code 
while running:
    screen.fill((150, 150, 150))

    clock.tick(60)  # limits frame rate, 30 clicks ~= 0.75 seconds
    textLen = 0
    for text in fadingTextEffect:
        if text[4] > 0:
            fadingTextEffect[textLen] = addText(text[0], gameFont, text[1], text[2], text[3], text[4])
        else:
            fadingTextEffect[text].remove()
        textLen += 1

    if start == True:
        fr += 1
        if fr % clicks[1] == 0:
            playsound("air.mp3",False)
            playsound("Met.mp3",False) # "put path of mp3 file (or name)"
            if fr == clicks[0]:
                fr = 0
                if listen:
                    listen = False
                else:
                    listen = True
    else:
        addText("Press space to start", startFont, "blue", sw/10, sh/3)
    
    # key binds and actions
    for event in pygame.event.get():

        keys=pygame.key.get_pressed()
        if start == True and not(listen):
            # note keys
            if keys[pygame.K_r]:
                if not(keyDowns[0]):
                    playsound("Drum.mp3", False)
                    print("r")
                    keyDowns[0] = True
                    if fr % clicks[1] <= 1 or fr % clicks[1] == (clicks[1] - 1):
                        fadingTextEffect.append(["Perfect", "green", sw/3, sh/3, 255])
                    elif fr % clicks[1] > (clicks[1] // 2):
                        fadingTextEffect.append(["Early", "blue", sw/3, sh/3, 255])
                    else:
                        fadingTextEffect.append(["Late", "red", sw/3, sh/3, 255])

            else:
                keyDowns[0] = False
            if keys[pygame.K_l]:
                if not(keyDowns[1]):
                    playsound("Drum.mp3", False)
                    print("l")
                    keyDowns[1] = True
                    if fr % clicks[1] <= 1 or fr % clicks[1] == (clicks[1] - 1):
                        fadingTextEffect.append(["Perfect", "green", sw/3, sh/3, 255])
                    elif fr % clicks[1] > (clicks[1] // 2):
                        fadingTextEffect.append(["Early", "blue", sw/3, sh/3, 255])
                    else:
                        fadingTextEffect.append(["Late", "red", sw/3, sh/3, 255])
            else:
                keyDowns[1] = False
        
        if start == False:
            if keys[pygame.K_SPACE]:
                start = True
        # quit
        if keys[pygame.K_ESCAPE]:
            print("|-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-|")
            running = False
    
    pygame.display.flip()