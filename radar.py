# Importing libraries
import pygame
from math import *
import time

# Initializing the game
pygame.init()
pygame.font.init()

# Defining colours and font
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Creating a screen
screen = pygame.display.set_mode((800, 650))


# Title and icon
pygame.display.set_caption('Radar')
icon = pygame.image.load('radar.png')
pygame.display.set_icon(icon)


# Creating a radar object
def radar(rect):
    pygame.draw.arc(screen, green, rect, 0, ((180.499999999999/180)*pi), 2)


# Drawing the radar object on the screen
def draw_radar():
    radar([300, 500, 200, 200])
    radar([200, 400, 400, 400])
    radar([100, 300, 600, 600])


# Creating a line object
def line(pos):
    pygame.draw.line(screen, green, (400, 600), pos)


# Drawing the lines for referencing angles
def draw_lines():
    line((700, 600))
    line((550, 340.2))
    line((659.8, 450))
    line((400, 300))
    line((250, 340.2))
    line((140.2, 450))
    line((100, 600))


# Drawing text text surface
def text(text, co_ord, size=35, font='Calibiri'):
    font = pygame.font.SysFont(font, size, bold=False, italic=True)
    text_surface = font.render(text, True, green)
    screen.blit(text_surface, co_ord)


# Displaying all text
def draw_text():
    text('0', (700, 580))
    text('30', (664.8, 433))
    text('60', (550, 320.2))
    text('90', (385, 275))
    text('120', (210, 315.2))
    text('150', (92.2, 435))
    text('180', (55, 580))
    text('20cm', (450, 600), 25)
    text('40cm', (550, 600), 25)
    text('60cm', (650, 600), 25)
    text('RADAR', (275, 50), 100)


# final static radar draw
def final_radar():
    draw_radar()
    draw_lines()
    draw_text()


# Generating the values of angles from 0 to 180 and back
# def radar_degree_gen():
#    while True:
#        for x in range(181):
#            yield x
#        for x in range(180, -1, -1):
#            yield x


# Creating a sweep action
# def radar_sweeper(pos, current_radar_deg):
#    angle = next(current_radar_deg)
#    end_pos = (pos[0] + 300*cos(radians(angle)), pos[1] - 300*sin(radians(angle)))
#    return end_pos


# Setting the speed of the sweep
clock = pygame.time.Clock()
fps = 60

# Setting the angle values
# current_radar_deg = radar_degree_gen()


def var_line(θ):
    x = 400 + 300*cos(radians(θ))
    y = 600 - 300*sin(radians(θ))
    pygame.draw.line(screen, green, (400, 600), (x, y))


θ = 0
ω = 30

# Starting the window
running = True

while running:
    sT = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    # Resets the screen every frame

    screen.fill([0, 0, 0])
    final_radar()
    # pos = (400, 600)
    # end_pos = radar_sweeper(pos, current_radar_deg)
    # pygame.draw.line(screen, green, pos, end_pos, 2)

    var_line(θ)
    if int(θ) == 0:
        ω = 30
    elif int(θ) == 180:
        ω = -30
    eT = time.time()
    θ += ω*(eT-sT)
    pygame.display.update()