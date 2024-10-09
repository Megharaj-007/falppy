import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')

# Load images
bird_image = pygame.image.load('C:/path/to/FLAPPY BIRD/Game Gallery/Flappy_Bird-PNG-Picture.png')  
pipe_image = pygame.image.load('C:/path/to/FLAPPY BIRD/Game Gallery/pipe.png')  

background_image = pygame.image.load('bg_5.png')  

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -10

# Pipe variables
pipe_width = 80
pipe_gap = 150
pipe_speed = 3
pipes = []
score = 0
font = pygame.font.Font(None, 36)

def create_pipe():
    height = random.randint(100, 400)
    top = pipe_image.get_rect(topleft=(WIDTH, height - pipe_image.get_height()))
    bottom = pipe_image.get_rect(topleft=(WIDTH, height + pipe_gap))
    return top, bottom

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Update bird
    bird_velocity += gravity
    bird_y += bird_velocity
    screen.blit(bird_image, (bird_x, bird_y))
    
    # Update pipes
    if len(pipes) == 0 or pipes[-1][0].x < WIDTH - 200:
        pipes.append(create_pipe())

    for pipe in pipes:
        pipe[0].x -= pipe_speed
        pipe[1].x -= pipe_speed
        screen.blit(pipe_image, pipe[0])
        screen.blit(pipe_image, pipe[1])

        # Collision detection
        if bird_x + bird_image.get_width() > pipe[0].x and bird_x < pipe[0].x + pipe_width:
            if bird_y < pipe[0].y + pipe_image.get_height() or bird_y + bird_image.get_height() > pipe[1].y:
                running = False

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0].x > -pipe_width]

    # Draw score
    score_display = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (WIDTH // 2, 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
