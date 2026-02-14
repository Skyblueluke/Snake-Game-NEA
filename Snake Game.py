import pygame

pygame.init()

# Flags
running = True
menu_run = True
difficulty_run = False
game_run = False
selected_difficulty = None

# Rects
start_button = pygame.Rect(346, 264, 112, 32)
difficulty_button = pygame.Rect(278, 465, 263, 30)
quit_button = pygame.Rect(345, 664, 109, 32)

easy_button = pygame.Rect(346, 254, 464-346, 285-254)
medium_button = pygame.Rect(317, 374, 496-317, 404-374)
hard_button = pygame.Rect(347, 495, 471-347, 526-495)
back_button = pygame.Rect(348, 614, 469-348, 644-614)

# Screen and colors
WIDTH, HEIGHT = 800, 800
green = (14,209,28)
black = (0,0,0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
header = pygame.font.SysFont("arialblack", 80)
font = pygame.font.SysFont("arialblack", 40)
text_colour = green

def write_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    SCREEN.blit(img, (x,y))

# Main loop
while running:
    SCREEN.fill(black)  # Clear screen at start of frame

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_run:
                if start_button.collidepoint(event.pos):
                    print("Play pressed")
                    menu_run = False
                    game_run = True
                elif difficulty_button.collidepoint(event.pos):
                    print("Difficulty pressed")
                    menu_run = False
                    difficulty_run = True
                    game_run = False
                elif quit_button.collidepoint(event.pos):
                    running = False
            elif difficulty_run:
                if easy_button.collidepoint(event.pos):
                    selected_difficulty = "Easy"
                    difficulty_run = False
                    menu_run = True
                elif medium_button.collidepoint(event.pos):
                    selected_difficulty = "Medium"
                    difficulty_run = False
                    menu_run = True
                elif hard_button.collidepoint(event.pos):
                    selected_difficulty = "Hard"
                    difficulty_run = False
                    menu_run = True
                elif back_button.collidepoint(event.pos):
                    difficulty_run = False
                    menu_run = True

    # Draw the appropriate menu
    if menu_run:
        write_text("SNAKE", header, text_colour, 250, 50)
        write_text("PLAY", font, text_colour, 345, 250)
        write_text("DIFFICULTY", font, text_colour, 275, 450)
        write_text("QUIT", font, text_colour, 345, 650)

        pygame.draw.rect(SCREEN, (255, 0, 0), start_button, 1)
        pygame.draw.rect(SCREEN, (0, 255, 0), difficulty_button, 1)  
        pygame.draw.rect(SCREEN, (0, 0, 255), quit_button, 1)

    elif difficulty_run:
        write_text("DIFFICULTY", header, text_colour, 150, 50)
        write_text("EASY", font, text_colour, 345, 240)
        write_text("MEDIUM", font, text_colour, 315, 360)
        write_text("HARD", font, text_colour, 345, 480)
        write_text("BACK", font, text_colour, 345, 600)

        pygame.draw.rect(SCREEN, (255,0,0), easy_button, 1)
        pygame.draw.rect(SCREEN, (255,255,0), medium_button, 1)
        pygame.draw.rect(SCREEN, (0,0,255), hard_button, 1)
        pygame.draw.rect(SCREEN, (0,255,255), back_button, 1)

    elif game_run:
        SCREEN.fill(black)

        write_text("SNAKE GAME", header, text_colour, 200, 50)

        if selected_difficulty is None:
            write_text("Difficulty: Not selected", font, text_colour, 200, 200)
        else:
            write_text("Difficulty:" + selected_difficulty, font, text_colour, 200, 200)

        write_text("Press ESC to return to menu", font, text_colour, 150, 400)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game_run:
                    game_run = False
                    menu_run = True

                        
    pygame.display.update()

pygame.quit()
