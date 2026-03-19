import pygame  # Imports pygame and pygame library

import random  # Imports random for the apples

pygame.init()  # Activates pygame

# Flags
running = True  # This is the whole game loop (always active)
menu_run = True  # This is the menu loop (currently active)
difficulty_run = False  # This is the difficuty loop (currently inactive)
game_run = False  # This is the playing lood (currently inactive)
pause_run = False  # This is for when the game is paused (currently inactive)
game_over = False  # This is for when the snake collides
selected_difficulty = "Medium"  # This is the game difficulty variable initially set at medium
snake_speed = 13  # This is the snake speed which is a linked variable to the difficulty
TOP_MARGIN = 80  # This leaves space for score/difficulty at top
high_score = 0  # This tracks the highest score achieved

# Snake settings
BLOCK_SIZE = 20  # This is the size of a single grid square in pixels
snake = [(400, 400), (380, 400),
         (360, 400)]  # The snake is a list of tuples, 1st tuple is the head and the other 2 are the body
direction = "RIGHT"  # This is the current direction of the snake
change_to = direction  # This stores the next direction

# Rects
play_button = pygame.Rect(346, 224, 112, 32)  # These are the play  button co ordinates
difficulty_button = pygame.Rect(278, 425, 263, 30)  # These are the difficulty button co ordinates
quit_button = pygame.Rect(345, 624, 109, 32)  # There are the quid button co ordinates

easy_button = pygame.Rect(346, 254, 464 - 346, 285 - 254)  # These are the easy  button co ordinates
medium_button = pygame.Rect(317, 374, 496 - 317, 404 - 374)  # These are the medium  button co ordinates
hard_button = pygame.Rect(347, 495, 471 - 347, 526 - 495)  # These are the play  hard co ordinates
back_button = pygame.Rect(348, 614, 469 - 348, 644 - 614)  # These are the play  back co ordinates

# Screen and colours
WIDTH, HEIGHT = 800, 680  # This is the window size
green = (14, 209, 28)  # This is green being established as a colour
black = (0, 0, 0)  # This is black being established as a colour
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # This is the screen being made
pygame.display.set_caption("Snake Game")  # This is the nig Snake Game message at the top of the screen

# Fonts
header = pygame.font.SysFont("arialblack", 80)  # This is the header font being established
font = pygame.font.SysFont("arialblack", 40)  # This is the standard font being established
ui_font = pygame.font.SysFont("arialblack", 25)  # This is the top corner font being established
text_colour = green  # This is the font colour being established


def write_text(text, font, text_colour, x, y):  # These are the the necessary parts of the funtion designed to make a new word on the screen
    img = font.render(text, True, text_colour)  # This writes the message
    SCREEN.blit(img, (x, y))  # This puts it on the screen


# Grid
BLOCK_SIZE = 20  # This is the size of a single grid square in pixels
snake = [(400, 400), (380, 400),
         (360, 400)]  # The snake is a list of tuples, 1st tuple is the head and the other 2 are the body
direction = "RIGHT"  # This is the current direction of the snake


# Apple making function
def spawn_apple():  # This makes the function 'spawn_apple'
    while True:  # While spawn_apple is true
        x = random.randrange(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  # Anywhere widthwise in the window
        y = random.randrange(TOP_MARGIN // BLOCK_SIZE, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  # Anywhere depthwise in the window but before the margin
        if (x, y) not in snake:  # If it is not on the snake
            return (x, y)  # Place it

snake = [(400, TOP_MARGIN + 3*BLOCK_SIZE), (380, TOP_MARGIN + 3*BLOCK_SIZE), (360, TOP_MARGIN + 3*BLOCK_SIZE)] # Snake tuple created below margin

# Clock
clock = pygame.time.Clock()  # This makes a clock that the game will run by

# Main loop
while running:  # This is the beginning of the actual loop - running is always True
    if not pause_run: # This keeps game clear when paused
        SCREEN.fill(black)  # Clear screen at start of frame

    # Event handling
    for event in pygame.event.get():  # This is the beginning of the loop that says if x happens do y
        ##        print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:  # This is for the quit button, it will end the program, and this ends the running loop
            running = False  # This is the end of the running loop

        # Moving the snake
        elif event.type == pygame.KEYDOWN:
            if game_run:  # If a key is pressed loop
                if event.key == pygame.K_w or event.key == pygame.K_UP:  # If w or up arrow is pressed
                    change_to = "UP"  # Change next snake direction to up
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # If s or down arrow is pressed
                    change_to = "DOWN"  # Change next snake direction to up
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # If a or left arrow is pressed
                    change_to = "LEFT"  # Change next snake direction to up
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # If d or right arrow is pressed
                    change_to = "RIGHT"  # Change next snake direction to up

                    # Pause the game
                elif event.key == pygame.K_p and game_run:  # If P pressed and game running
                    game_run = False  # Stop game loop
                    pause_run = True  # Start paused loop

            # Unpause the game
            elif event.key == pygame.K_p and pause_run:  # If P pressed and game paused
                pause_run = False  # Stop pause loop
                game_run = True  # Start game loop
            # End the game from the pause menu

            # Ending the game from the pause menu
            elif event.key == pygame.K_ESCAPE and pause_run:  # If ESC pressed and game paused
                pause_run = False  # Stop pause loop
                menu_run = True  # Start menu loop




        elif event.type == pygame.MOUSEBUTTONDOWN:  # If the mouse is clicked loop
            if menu_run:  # This is the menu loop, it is also the loop that origninally starts due to it being True initially in the flags section
                if play_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the play button (established in the rects section)
                    print(
                        "Play pressed")  # This was for checking if the button was recognised as pressed before there were menu changes
                    menu_run = False  # Menu loop ends
                    game_run = True  # Playing loop starts
                    apple_pos = spawn_apple()  # This is the start of the apple spawning process
                elif difficulty_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the difficulty button (established in the rects section)
                    print(
                        "Difficulty pressed")  # This was for checking if the button was recognised as pressed before there were menu changes
                    menu_run = False  # Menu loop ends
                    difficulty_run = True  # Difficulty menu loop starts
                elif quit_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the play button (established in the rects section)
                    running = False  # Whole game loop ends
            elif difficulty_run:  # If the difficulty menu loop is active
                if easy_button.collidepoint(
                        event.pos):  # # If the mouse is clicked on the easy button (established in the rects section)
                    selected_difficulty = "Easy"  # The difficulty is set to easy
                    ##                    difficulty_run = False  # Difficulty menu loop ends
                    ##                    menu_run = True  # Menu loop starts again
                    snake_speed = 8  # This is the snakes speed in the easy difficulty
                elif medium_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the medium button (established in the rects section)
                    selected_difficulty = "Medium"  # The difficulty is set to medium
                    ##                    difficulty_run = False  # Difficulty menu loop ends
                    ##                    menu_run = True  # Menu loop starts again
                    snake_speed = 13  # This is the snakes speed in the medium difficulty
                elif hard_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the hard button (established in the rects section)
                    selected_difficulty = "Hard"  # The difficulty is set to hard
                    ##                    difficulty_run = False  # Difficulty menu loop ends
                    ##                    menu_run = True  # Menu loop starts again
                    snake_speed = 18  # This is the snakes speed in the hard difficulty
                elif back_button.collidepoint(
                        event.pos):  # If the mouse is clicked on the back button (established in the rects section)
                    difficulty_run = False  # Difficulty menu loop ends
                    menu_run = True  # Menu loop starts again

                # Game over event
                if event.type == pygame.KEYDOWN:  # If a key is pressed loop
                    if game_over and event.key == pygame.K_SPACE:  # If game over and space bar pressed
                        game_over = False  # Game over loop ends
                        menu_run = True  # Menu loop restarts
                        snake = [(400, 400), (380, 400), (360, 400)]  # Snake position resets
                        direction = "RIGHT"  # Current direction resets
                        change_to = direction  # Next direction resets
                        apple_pos = spawn_apple()  # Apples resets

    # Draw the appropriate menu
    if menu_run:  # If the menu loop is running
        write_text("SNAKE", header, text_colour, 250,
                   50)  # Write SNAKE in the header font (established in the fonts section)
        write_text("PLAY", font, text_colour, 345,
                   210)  # Write PLAY in the standard font (established in the fonts section)
        write_text("DIFFICULTY", font, text_colour, 275,
                   410)  # Write DIFFICULTY in the standard font (established in the fonts section)
        write_text("QUIT", font, text_colour, 345,
                   610)  # Write QUIT in the standard font (established in the fonts section)

    ##        pygame.draw.rect(SCREEN, (255, 0, 0), play_button, 1) # Makes a hitbox in red around the play button for debugging purposes
    ##        pygame.draw.rect(SCREEN, (0, 255, 0), difficulty_button, 1) # Makes a hitbox in red around the difficulty button for debugging purposes
    ##        pygame.draw.rect(SCREEN, (0, 0, 255), quit_button, 1) # Makes a hitbox in red around the quit button for debugging purposes

    elif difficulty_run:  # If the difficulty loop is running
        write_text("DIFFICULTY", header, text_colour, 150,
                   50)  # Write DIFFICULTY in the header font (established in the fonts section)
        write_text("EASY", font, text_colour, 345,
                   240)  # Write EASY in the standard font (established in the fonts section)
        write_text("MEDIUM", font, text_colour, 315,
                   360)  # Write MEDIUM in the standard font (established in the fonts section)
        write_text("HARD", font, text_colour, 345,
                   480)  # Write HARD in the standard font (established in the fonts section)
        write_text("BACK", font, text_colour, 345,
                   600)  # Write BACK in the standard font (established in the fonts section)

        # Highlight selected difficulty
        if selected_difficulty == "Easy":  # If easy difficulty is selected
            highlight = easy_button.inflate(60, 20)  # Grow the hitbox
            pygame.draw.rect(SCREEN, green, highlight, 3)  # Make hitbox in easy green

        elif selected_difficulty == "Medium":  # If medium difficulty is selected
            highlight = medium_button.inflate(30, 20)  # Grow the hitbox
            pygame.draw.rect(SCREEN, green, highlight, 3)  # Make hitbox in medium green

        elif selected_difficulty == "Hard":  # If hard difficulty is selected
            highlight = hard_button.inflate(30, 20)  # Grow the hitbox
            pygame.draw.rect(SCREEN, green, highlight, 3)  # Make hitbox in hard green

    ##        pygame.draw.rect(SCREEN, (255,0,0), easy_button, 1) # Makes a hitbox in red around the easy button for debugging purposes
    ##        pygame.draw.rect(SCREEN, (255,255,0), medium_button, 1) # Makes a hitbox in red around the medium button for debugging purposes
    ##        pygame.draw.rect(SCREEN, (0,0,255), hard_button, 1) # Makes a hitbox in red around the hard button for debugging purposes
    ##        pygame.draw.rect(SCREEN, (0,255,255), back_button, 1) # Makes a hitbox in red around the back button for debugging purposes

    elif game_run:  # If the playing loop is running
        SCREEN.fill(black)  # Make the whole window black
        pygame.draw.line(SCREEN, green, (0, TOP_MARGIN), (WIDTH, TOP_MARGIN), 2) # Make green margin  line 

        write_text("Score: " + str(len(snake) - 3), ui_font, green, 10, 10)  # This is the score in the top corner
        write_text("Difficulty: " + selected_difficulty, ui_font, green, 10,
                   50)  # This is the difficulty in the top corner
        write_text(f"High Score: {high_score}", ui_font, green, 600, 10) # This is the high score in the top corner

        score = len(snake) - 3  # Current game score
        if score > high_score:   # Update high score if beaten
            high_score = score # New high score
        # Making the snake
        for segment in snake:  # This established the snake as a list of segments (These segments will becom ea tuple)
            pygame.draw.rect(SCREEN, green, pygame.Rect(segment[0], segment[1], BLOCK_SIZE,
                                                        BLOCK_SIZE))  # Draws a green recangle on the screen with a tuple of segments

            # Making the apple
            pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], BLOCK_SIZE,
                                                              BLOCK_SIZE))  # Draws a red square on the screen as a single segment

        # Stopping illegal moves
        if change_to == "UP" and direction != "DOWN":  # If the direction is up and next direction is not down
            direction = "UP"  # Make new direction up
        elif change_to == "DOWN" and direction != "UP":  # If the direction is down and next direction is not up
            direction = "DOWN"  # Make new direction down
        elif change_to == "LEFT" and direction != "RIGHT":  # If the direction is left and next direction is not right
            direction = "LEFT"  # Make new direction left
        elif change_to == "RIGHT" and direction != "LEFT":  # If the direction is right and next direction is not left
            direction = "RIGHT"  # Make new direction right
            # This means the snake will only move legally

            # Move snake head
        x, y = snake[0]  # This splits the snake's head into an x and y co ordinate

        if direction == "UP":  # If the current direction is up
            y -= BLOCK_SIZE  # Y co ordinate decreases
        elif direction == "DOWN":  # If the current direction is up
            y += BLOCK_SIZE  # Y co ordinate increases
        elif direction == "LEFT":  # If the current direction is up
            x -= BLOCK_SIZE  # X co ordinate decreases
        elif direction == "RIGHT":  # If the current direction is up
            x += BLOCK_SIZE  # X co ordinate increases

            ##            x, y = snake[0] # This is the current head
            ##
            ##            if direction == "UP": # If the current direction is up
            ##                y -= BLOCK_SIZE # Y co ordinate decreases
            ##            elif direction == "DOWN": # If the current direction is down
            ##                y += BLOCK_SIZE # Y co ordinate increases
            ##            elif direction == "LEFT": # If the current direction is left
            ##                x -= BLOCK_SIZE # X co ordinate decreases
            ##            elif direction == "RIGHT": # If the current direction is right
            ##                x += BLOCK_SIZE # X co ordinate increases
            ##
            # Wall collision
            ##        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT: # If past left - right or top - bottom
            ##            print("You hit a wall!") # Hit wall
            ##            game_run = False # Playing loop ends
            ##            game_over = True # Game over loop starts
            ##            snake = [(400, 400), (380, 400), (360, 400)]  # Snake position resets
            ##            direction = "RIGHT"  # Direction resets to right
            ##            change_to = direction # Next direction becomes current direction
            ##            apple_pos = spawn_apple()  # Apples reset
            ##
            ##        # Snake on snake collision
            ##        elif (x, y) in snake: # If head is in snake
            ##            game_run = False  # Playing loop ends
            ##            game_over = True   # Game over loop starts
            ##            snake = [(400, 400), (380, 400), (360, 400)]  # Snake position resets
            ##            direction = "RIGHT"  # Direction resets to right
            ##            change_to = direction # Next direction becomes current direction
            ##            apple_pos = spawn_apple()  # Apples reset
            ##            continue # This makes the reset actually happen

        if x < 0 or x >= WIDTH or y < TOP_MARGIN or y >= HEIGHT or (x, y) in snake:  # If out of bounds or huit self
            print(
                "You hit the wall!" if x < 0 or x >= WIDTH or y < TOP_MARGIN or y >= HEIGHT else "You hit yourself!") # If you hit yourself or the wall
            game_run = False  # Playing loop ends
            game_over = True  # Game loop starts again
            
            if game_over:  # If game over loop is active
                SCREEN.fill(black)  # Fill the whole screen as black
                write_text("GAME OVER", header, green, 120, 200)  # Game over message with premade header font
                write_text(f"SCORE: {len(snake) - 3}", font, green, 290,
                            320)  # Display score in normal premade font
                write_text("PRESS SPACE TO RETURN TO MENU", font, green, 1, 400)  # Message in normal premade font
                pygame.display.update()  # Update the screens display
                waiting = True  # Waitingf= for player to press spacebar
                while waiting:  # While waiting loop is active
                    for event in pygame.event.get():  # If event loop
                        if event.type == pygame.QUIT:  # If player quits
                            running = False  # Running (main) loop stops
                            waiting = False  # Spacebar loop stops
                        if event.type == pygame.KEYDOWN:  # If spacebar pressed loop
                            if event.key == pygame.K_SPACE:  # Spacebar loop active
                                game_over = False  # Game over loop ends
                                waiting = False  # Waiting loop ends
                                menu_run = True  # Menu loop restars
                                game_run = False  # Playing loop ends
                                continue  # This makes the reset actually happen
            snake = [(400, 400), (380, 400), (360, 400)]  # Snake position and size resents
            direction = "RIGHT"  # Direction resets
            change_to = direction  # Next direction resets
            apple_pos = spawn_apple()  # New apple spawns
            game_over = False  # Game over loop ends
            continue  # This makes the reset actually happen

        new_head = (x, y)  # This makes the new head
        snake.insert(0, new_head)  # This visually adds it

            
        # Apple collision
        if new_head == apple_pos:  # If the apple and snake collide
            apple_pos = spawn_apple()  # The snake grows
        else:  # If the apple and the snake do not collide
            snake.pop()  # This removes the final part of the tail, giving the illusion that the snake moves

        clock.tick(snake_speed)  # The clock is directly linked the the difficulty and snake speed


        for segment in snake:  # For each part of the snake
            pygame.draw.rect(SCREEN, green, pygame.Rect(segment[0], segment[1], BLOCK_SIZE,
                                                            BLOCK_SIZE))  # This draws a green tuple-based rectangle



        # elif pause_run:  # Pause menu

    elif pause_run:  # Pause menu

        for segment in snake:  # For each part of the snake
                pygame.draw.rect(SCREEN, green, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))  # This draws a green tuple-based rectangle (snake)
                pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], BLOCK_SIZE, BLOCK_SIZE)) # This creates a red square (apple)

        write_text("Score: " + str(len(snake) - 3), ui_font, green, 10, 10)  # This is the score in the top corner
        write_text("Difficulty: " + selected_difficulty, ui_font, green, 10,
                   50)  # This is the difficulty in the top corner
        write_text(f"High Score: {high_score}", ui_font, green, 600, 10) # This is the high score in the top corner

        pygame.draw.line(SCREEN, green, (0, TOP_MARGIN), (WIDTH, TOP_MARGIN), 2) # Make green margin  line 

    
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # this has the window size (stored) and colour and trnnsparency key
        overlay.fill((0, 0, 0, 150))  # this makes a semi-transparent black
        SCREEN.blit(overlay, (0, 0))  # this draws the overlay

        write_text("PAUSED", header, green, 200, 200) # Write PAUSED in the header font (established in the fonts section)
        write_text("PRESS P TO RESUME", font, green, 150, 350)  # Write PRESS P TO RESUME in the standard font (established in the fonts section)
        write_text("PRESS ESC FOR MENU", font, green, 150, 420)  # Write PRESS ESC FOR MENU in the standard font (established in the fonts section)

    pygame.display.update()  # This commands the screen to update at all times in the main loop

pygame.quit()  # Closes the program
