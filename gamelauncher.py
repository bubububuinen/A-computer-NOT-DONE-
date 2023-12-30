pip install pygame
# launcher.py

import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Launcher")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Simple text rendering function
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Game list
games = [
    {"name": "Game 1", "module": "game1"},
    {"name": "Game 2", "module": "game2"},
    # Add more games as needed
]

# Main game loop
while True:
    screen.fill(white)

    # Draw game list
    for i, game in enumerate(games):
        draw_text(game["name"], 36, black, 400, 200 + i * 50)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, game in enumerate(games):
                if 400 - 100 < x < 400 + 100 and 200 + i * 50 - 25 < y < 200 + i * 50 + 25:
                    # Launch the selected game
                    pygame.quit()
                    os.system(f"python -m {game['module']}")  # Run the selected game module
                    sys.exit()
