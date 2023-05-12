import pygame
import random

# initialize pygame
pygame.init()

# set the window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the title of the window
pygame.display.set_caption("Flappy Bird")

# set the clock for the game
CLOCK = pygame.time.Clock()

# load the bird image
BIRD_IMAGE = pygame.image.load("bird.png")
BIRD_RECT = BIRD_IMAGE.get_rect()

# load the pipe image
PIPE_IMAGE = pygame.image.load("pipe.png")
PIPE_RECT = PIPE_IMAGE.get_rect()

# set the gravity and jump speed
GRAVITY = 0.5
JUMP_SPEED = -10

# set the score font
SCORE_FONT = pygame.font.Font(None, 50)

# function to generate pipes
def generate_pipes():
    pipe_x = WINDOW_WIDTH
    pipe_gap = 150
    pipe_height = random.randint(50, WINDOW_HEIGHT - pipe_gap - 50)
    top_pipe_rect = PIPE_RECT.copy()
    top_pipe_rect.bottom = pipe_height
    top_pipe_rect.left = pipe_x
    bottom_pipe_rect = PIPE_RECT.copy()
    bottom_pipe_rect.top = pipe_height + pipe_gap
    bottom_pipe_rect.left = pipe_x
    return [top_pipe_rect, bottom_pipe_rect]

# initialize the game variables
bird_y = WINDOW_HEIGHT / 2
bird_speed = 0
pipes = []
score = 0

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = JUMP_SPEED

    # update the bird
    bird_speed += GRAVITY
    bird_y += bird_speed
    BIRD_RECT.top = bird_y

    # generate new pipes
    if len(pipes) == 0 or pipes[-1].left < WINDOW_WIDTH - 200:
        pipes.extend(generate_pipes())

    # move the pipes
    for pipe in pipes:
        pipe.left -= 5

    # remove pipes that are off the screen
    if pipes[0].right < 0:
        pipes.pop(0)

    # check for collisions
    for pipe in pipes:
        if BIRD_RECT.colliderect(pipe):
            pygame.quit()
            exit()

    # check for score
    if pipes[0].right < BIRD_RECT.left:
        pipes.pop(0)
        score += 1

    # draw the background
    WINDOW.fill((0, 0, 0))

    # draw the bird
    WINDOW.blit(BIRD_IMAGE, BIRD_RECT)

    # draw the pipes
    for pipe in pipes:
        WINDOW.blit(PIPE_IMAGE, pipe)

    # draw the score
    score_text = SCORE_FONT.render(str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.topright = (WINDOW_WIDTH - 10, 10)
    WINDOW.blit(score_text, score_rect)

    # update the window
    pygame.display.update()

    # set the frame rate
    CLOCK.tick(60)
