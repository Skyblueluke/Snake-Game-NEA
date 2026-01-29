import pygame

pygame.init()

WIDTH = 800
HEIGHT =800

green = (14,209,28)
black = (0,0,0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Main Menu")
#This creates the window

font = pygame.font.SysFont("arialblack", 40)

## NOTE ##
##font = pygame.font.Sysfont("FONT", SIZE)##
#This defines the fonts

text_colour = (green)
#This defines the text colour

def write_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    SCREEN.blit(img, (x,y))
#function defined for writing the text

menu_run = True
while menu_run:
#This starts the lood in which the menu runs from

    SCREEN.fill(black)

    write_text("Press SPACE to continue", font, text_colour,135, 350)

## NOTE ##
##write_text("MESSAGE", FONT(arialblack, SIZE: 40), COLOUR: (22, 82, 3), x CO-ORDINATE: 0,y CO-ORDINATE: 0)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_run = False

    pygame.display.update()
    
pygame.quit()

#This quits the program on request
