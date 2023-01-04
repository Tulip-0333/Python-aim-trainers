import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
screen_size = (800, 600)

# Set the window title
pygame.display.set_caption('Aim Trainer')

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Set the background color
bg_color = (0, 0, 0)

# Set the circle color
circle_color = (255, 255, 255)

# Set the circle radius
circle_radius = 20

# Set the circle position
circle_pos = [random.randint(circle_radius, screen_size[0] - circle_radius), random.randint(circle_radius, screen_size[1] - circle_radius)]

# Set the circle speed
circle_speed = [2, 2]

# Set the font
font = pygame.font.Font(None, 36)

# Set the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Check for mouse collision with the circle
            if (mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2 <= circle_radius ** 2:
                # Set the circle position to a random position
                circle_pos = [random.randint(circle_radius, screen_size[0] - circle_radius), random.randint(circle_radius, screen_size[1] - circle_radius)]
                # Set the circle speed to a random speed
                circle_speed = [random.randint(-5, 5), random.randint(-5, 5)]



    # Move the circle
    circle_pos[0] += circle_speed[0]
    circle_pos[1] += circle_speed[1]

    # Check for collision with the walls
    if circle_pos[0] - circle_radius <= 0 or circle_pos[0] + circle_radius >= screen_size[0]:
        circle_speed[0] = -circle_speed[0]
    if circle_pos[1] - circle_radius <= 0 or circle_pos[1] + circle_radius >= screen_size[1]:
        circle_speed[1] = -circle_speed[1]

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check for mouse collision with the circle
    if (mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2 <= circle_radius ** 2:
        circle_color = (0, 255, 0)
    else:
        circle_color = (255, 255, 255)

    # Draw the background
    screen.fill(bg_color)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    # Draw the text
    text = font.render('Aim Trainer', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (screen_size[0] // 2, screen_size[1] // 2)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)
