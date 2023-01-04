import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
screen_size = (1920, 1080)

# Set the window title
pygame.display.set_caption('Aim Trainer')

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Set the background color
bg_color = (0, 0, 0)

# Set the circle radius
circle_radius = 100

# Set the font
font = pygame.font.Font(None, 36)

# Set the clock
clock = pygame.time.Clock()

# Set the number of circles
num_circles = 1

# Load the crosshair image
crosshair_image = pygame.image.load('crosshair.png')

# Get the crosshair image
crosshair_image_size = crosshair_image.get_size()


# Set the mouse cursor to be invisible
pygame.mouse.set_visible(False)

# Create the circles
circles = []
for i in range(num_circles):
    # Set the circle color
    circle_color = (255, 255, 255)

    # Set the circle position
    circle_pos = [random.randint(circle_radius, screen_size[0] - circle_radius), random.randint(circle_radius, screen_size[1] - circle_radius)]

    # Set the circle speed
    circle_speed = [random.randint(-5, 5), random.randint(-5, 5)]

    # Create the circle
    circle = {
        'color': circle_color,
        'pos': circle_pos,
        'speed': circle_speed,
        'radius': circle_radius
    }

    # Add the circle to the list
    circles.append(circle)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Check for mouse collision with the circles
            for circle in circles:
                if (mouse_pos[0] - circle['pos'][0]) ** 2 + (mouse_pos[1] - circle['pos'][1]) ** 2 <= circle['radius'] ** 2:
                    # Set the circle position to a random position
                    circle['pos'] = [random.randint(circle['radius'], screen_size[0] - circle['radius']), random.randint(circle['radius'], screen_size[1] - circle['radius'])]
                    # Set the circle speed to a random speed
                    circle['speed'] = [random.randint(-5, 5), random.randint(-5, 5)]

    # Update the circles
    for circle in circles:
        # Move the circle
        circle['pos'][0] += circle['speed'][0]
        circle['pos'][1] += circle['speed'][1]

        # Check for collision with the walls
        if circle['pos'][0] - circle['radius'] <= 0 or circle['pos'][0] + circle['radius'] >= screen_size[0]:
            circle['speed'][0] = -circle['speed'][0]
        if circle['pos'][1] - circle['radius'] <= 0 or circle['pos'][1] + circle['radius'] >= screen_size[1]:
            circle['speed'][1] = -circle['speed'][1]
    # Draw the background
    screen.fill(bg_color)

    # Draw the crosshair
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(crosshair_image, (mouse_pos[0] - crosshair_image_size[0] // 2, mouse_pos[1] - crosshair_image_size[1] // 2))

    # Draw the circles
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])

    # Draw the text
    text = font.render('Aim Trainer', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (screen_size[0] // 2, screen_size[1] // 2)
    screen.blit(text, text_rect)

    # Draw the circles
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])

    # Draw the text
    text = font.render('Aim Trainer', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (screen_size[0] // 2, screen_size[1] // 2)
    screen.blit(text, text_rect)


    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

