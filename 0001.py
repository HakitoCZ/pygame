#!/usr/bin/python3
'''
Start date: 15.Jun.2k14
Author: HakitoCZ
Origin: bMt47wvK6u0
Editor: Vim
Indent set to 2 spaces. I may be wrong but I feel it clearer that way.
'''

import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, *groups):
    super(Player, self).__init__(*groups)
    self.image = pygame.image.load('player.png')
    self.rect = pygame.rect.Rect((320, 200), self.image.get_size())

  def update(self, dt):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
      self.rect.x -= 150 * dt
    if key[pygame.K_RIGHT]:
      self.rect.x += 150 * dt
    if key[pygame.K_UP]:
      self.rect.y -= 150 * dt
    if key[pygame.K_DOWN]:
      self.rect.y += 150 * dt
        # movement speed 150px/s

class Game(object):
  def main(self, screen):
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    self.player = Player(sprites)

    while 1:
      dt = clock.tick(30)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
          return


      sprites.update(dt / 1000.)
        # change in time - in seconds
      screen.fill((200, 200, 200))
      sprites.draw(screen)
      pygame.display.flip()

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640, 400))
  Game().main(screen)

