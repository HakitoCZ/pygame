#!/usr/bin/python3

'''
15.Jun.2014, HakitoCZ, Manchester, UK
According tutor@bMt47wvK6u0
Very first pygame thing.
'''

import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, *groups):
    super(Player, self).__init__(*groups)
    self.image = pygame.image.load('player.png')
    self.rect = pygame.rect.Rect((320, 200), self.image.get_size())

  def update(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
      image_x -= 10
    if key[pygame.K_RIGHT]:
      image_x += 10
    if key[pygame.K_UP]:
      image_y -= 10
    if key[pygame.K_DOWN]:
      image_y += 10

class Game(object):
  def main(self,screen):
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    self.player = Player(sprites)

    while 1:
      clock.tick(30)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          return

      
      sprites.update()
      screen.fill((200, 200, 200))
      sprites.draw(screen)
      pygame.display.flip()

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640, 400))
  Game().main(screen)
