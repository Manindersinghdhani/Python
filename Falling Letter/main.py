import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Letter Fall Game")

# Background color
background_color = (21, 34, 56)

# Load fonts
font = pygame.font.Font(None, 48)

# Load sounds
correct_sound = pygame.mixer.Sound("correct_sound.mp3")
wrong_sound = pygame.mixer.Sound("wrong_sound.mp3")

# Letter variables
letter_size = 70
falling_speed = 0.40
fallen_letter = None
falling_letters = []

# Score variables
score_correct = 0
score_wrong = 0

# Function to create a new falling letter
def create_falling_letter():
    letter = chr(random.randint(65, 90))
    color = random.choice([(0, 255, 0), (255, 0, 0)])  # Green or red color
    x = random.randint(0, window_width - letter_size)
    y = -letter_size  # Start from the top of the window
    return {"letter": letter, "color": color, "x": x, "y": y}

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if fallen_letter is not None:
                typed_letter = event.unicode.upper()  # Convert typed letter to uppercase
                if typed_letter == fallen_letter["letter"]:
                    if fallen_letter["color"] == (0, 255, 0):
                        score_correct += 1
                        pygame.mixer.Sound.play(correct_sound)
                    else:
                        score_wrong += 1
                        pygame.mixer.Sound.play(wrong_sound)
                    fallen_letter = None
                else:
                    score_wrong += 1
                    pygame.mixer.Sound.play(wrong_sound)
                    fallen_letter = None

    # Fill the background
    window.fill(background_color)

    # Display scores
    score_correct_text = font.render("Correct: " + str(score_correct), True, (0, 255, 0))
    score_correct_rect = score_correct_text.get_rect()
    score_correct_rect.topleft = (10, 10)
    window.blit(score_correct_text, score_correct_rect)

    score_wrong_text = font.render("Wrong: " + str(score_wrong), True, (255, 0, 0))
    score_wrong_rect = score_wrong_text.get_rect()
    score_wrong_rect.topright = (window_width - 10, 10)
    window.blit(score_wrong_text, score_wrong_rect)

    # Create falling letter
    if fallen_letter is None or fallen_letter["y"] > window_height:
        fallen_letter = create_falling_letter()

    # Update and draw falling letter
    if fallen_letter is not None:
        # Update letter position
        fallen_letter["y"] += falling_speed

        # Draw the letter with the randomly selected color
        text = font.render(fallen_letter["letter"], True, fallen_letter["color"])
        window.blit(text, (fallen_letter["x"], fallen_letter["y"]))

        # Check if the letter reached the bottom
        if fallen_letter["y"] + letter_size > window_height:
            fallen_letter = None

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()