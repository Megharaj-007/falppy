import random 
import sys
import pygame
from pygame.locals import * 

def Welcomescreen():
    print("Welcome")
    
fps = 32
screenwidth = 298
screenheight = 511
screen = pygame.display.set_mode((screenwidth,screenheight))

groundy = screenwidth * 0.8
game_sprite = {}
game_sound = {}

#asset of game 
player = '/python game/Flappy bird/Game Gallery/Flappy-Bird-PNG.png'
background = '/python game/Flappy bird/Game Gallery/bg_5.png'
pipe = '/python game/Flappy bird/Game Gallery/pipe.png'


if __name__ == "__main__":
    pygame.init()
    fpsclock = pygame.time.Clock()
    pygame.display.set_caption('Flappy bird game by IS ke bacche')
    game_sprite['numbers'] = (
        pygame.image.load('python game/Flappy Bird/Game Gallery/1-Number-PNG.png').convert_alpha(),
        pygame.image.load('python game/Flappy Bird/Game Gallery/2-Number-PNG.png').convert_alpha(),
        pygame.image.load('Flappy bird/Game Gallery/3-Number-PNG.png').convert_alpha(),
    )


game_sprite['message'] = pygame.image.load('/python game/Flappy bird/Game Gallery/messaage.png').convert_alpha()
game_sprite['pipe'] = pygame.image.load('/python game/Flappy bird/Game Gallery/pipe.png').convert_alpha()

#Game souund to be added 




#end
game_sprite['player'] = pygame.image.load('player').convert_alpha()
game_sprite['background'] = pygame.image.load('background').convert_alpha()

while True:
    Welcomescreen()