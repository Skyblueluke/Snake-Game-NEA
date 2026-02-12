import pygame

pygame.init()

menu_run = True
difficulty_run = False
game_run = False
selected_difficulty = None



start_button = pygame.Rect(346, 264, 112, 32)
difficulty_button = pygame.Rect(278, 465, 263, 30)
quit_button = pygame.Rect(345, 664, 109, 32)

easy_button = pygame.Rect(345, 250, 100, 40)
medium_button = pygame.Rect(345, 350, 130, 40)
hard_button = pygame.Rect(345, 450, 100, 40)
back_button = pygame.Rect(345, 600, 100, 40)



WIDTH = 800
HEIGHT =800

green = (14,209,28)
black = (0,0,0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Snake Game")
#This creates the window

header = pygame.font.SysFont("arialblack", 80)

font = pygame.font.SysFont("arialblack", 40)

## NOTE ##
##font = pygame.font.Sysfont("FONT", SIZE)##
#This defines the fonts

text_colour = (green)
#This defines the text colour

def write_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    SCREEN.blit(img, (x,y))
#function defined for writing the text  displayed in the menu








#Main menu starts here


while menu_run:
    SCREEN.fill(black)

    write_text("SNAKE", header, text_colour,250, 50)
    write_text("PLAY", font, text_colour,345, 250)
    write_text("DIFFICULTY", font, text_colour,275, 450)
    write_text("QUIT", font, text_colour,345, 650)

    #These are the words on the screen

    pygame.draw.rect(SCREEN, (255, 0, 0), start_button, 1)
    pygame.draw.rect(SCREEN, (0, 255, 0), difficulty_button, 1)  
    pygame.draw.rect(SCREEN, (0, 0, 255), quit_button, 1)

    #Tyhese are the hitboxes for debugging

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print("Play pressed")
                menu_run = False
                game_run = True
            elif difficulty_button.collidepoint(event.pos):
                print("Difficulty pressed")
                menu_run = False
                difficulty_run = True
            elif quit_button.collidepoint(event.pos):
                menu_run = False

    pygame.display.update()


    #quit button has been clicked -> program killed
    #PLAY Cords = x = 346 to 458 and y = 296 to 264#
    write_text("DIFFICULTY", font, text_colour,275, 450)
    #DIFFICULTY cords = x = 278 to 541 and y = 465 to 495#
    write_text("QUIT", font, text_colour,345, 650)
    #QUIT Cords = x = 345 to 454 and y = 664 to 696#
    
## NOTE ##
##write_text("MESSAGE", FONT(arialblack, SIZE: 40), COLOUR: (22, 82, 3), x CO-ORDINATE: 0,y CO-ORDINATE: 0)##





#Difficulty menu starts here










# DIFFICULTY MENU LOOP
while difficulty_run:
    SCREEN.fill(black)
    write_text("DIFFICULTY", header, text_colour,150, 50)
    write_text("EASY", font, text_colour,345, 240)
    write_text("MEDIUM", font, text_colour,315, 360)
    write_text("HARD", font, text_colour,345, 480)
    write_text("BACK", font, text_colour,345, 600)


    # debug rectangles
##    pygame.draw.rect(SCREEN, (255,0,0), easy_button, 1)
##    pygame.draw.rect(SCREEN, (255,255,0), medium_button, 1)
##    pygame.draw.rect(SCREEN, (0,0,255), hard_button, 1)
##    pygame.draw.rect(SCREEN, (0,255,255), back_button, 1)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            difficulty_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button.collidepoint(event.pos):
                selected_difficulty = "Easy"
                difficulty_run = False
                game_run = True
            elif medium_button.collidepoint(event.pos):
                selected_difficulty = "Medium"
                difficulty_run = False
                game_run = True
            elif hard_button.collidepoint(event.pos):
                selected_difficulty = "Hard"
                difficulty_run = False
                game_run = True
            elif back_button.collidepoint(event.pos):
                difficulty_run = False
                menu_run = True  # go back to main menu

    pygame.display.update()










#End of co ordinate code#
    
pygame.quit()

#This quits the program on request




















    # debug rectangles
##    pygame.draw.rect(SCREEN, (255,0,0), easy_button, 1)
##    pygame.draw.rect(SCREEN, (255,255,0), medium_button, 1)
##    pygame.draw.rect(SCREEN, (0,0,255), hard_button, 1)
##    pygame.draw.rect(SCREEN, (0,255,255), back_button, 1)
