#!/usr/bin/python3
'''
Start date: 15.Jun.2k14
Author: HakitoCZ
Origin: bMt47wvK6u0
Indent set to 2 spaces. I may be wrong but I feel it clearer that way.
'''

import pygame


class Game(object):
  def main(self, screen):
    image = pygame.image.load('player.png')

    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
          return

      screen.fill((200, 200, 200))
      screen.blit(image, (320, 200))
        # in the middle
      pygame.display.flip()
        # flip drawing and displaying buffers
        # basicly vsync

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640, 400))
  Game().main(screen)

