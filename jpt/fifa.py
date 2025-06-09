import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Football Players Viewer")

# Camera settings
camera_x = 0
camera_y = 0
SCROLL_SPEED = 5

# Load player images
def load_player_image(path, size=(100, 100)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

# Create player objects
players = [
    {
        "image": load_player_image("messi.png"),  # Replace with actual path
        "x": 500,
        "y": 300
    },
    {
        "image": load_player_image("ronaldo.png"),  # Replace with actual path
        "x": 800,
        "y": 500
    },
    {
        "image": load_player_image("neymar.png"),  # Replace with actual path
        "x": 200,
        "y": 600
    }
]

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))  # White background
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input for scrolling
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        camera_y += SCROLL_SPEED  # Scroll up
    if keys[pygame.K_s]:
        camera_y -= SCROLL_SPEED  # Scroll down
    if keys[pygame.K_a]:
        camera_x += SCROLL_SPEED  # Scroll left
    if keys[pygame.K_d]:
        camera_x -= SCROLL_SPEED  # Scroll right
    
    # Draw all players relative to camera position
    for player in players:
        screen_x = player["x"] + camera_x
        screen_y = player["y"] + camera_y
        screen.blit(player["image"], (screen_x, screen_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()