# Basic Pygame Template

# contains filler values

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import sys
import pygame

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
  while True:
    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Constants

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Application Name | Asianguy_123')
bg_colour = pygame.Color('#FFFFFF')

# ---------------------------------------------------------------------------------------------------------------------
# Runs Code

if __name__ == '__main__':
  main()
