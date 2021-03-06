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

  def update(self, dt, game):
    last = self.rect.copy()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_h]:
      self.rect.x -= 250 * dt
    if key[pygame.K_RIGHT] or key[pygame.K_l]:
      self.rect.x += 250 * dt
    if key[pygame.K_UP] or key[pygame.K_k]:
      self.rect.y -= 250 * dt
    if key[pygame.K_DOWN] or key[pygame.K_j]:
      self.rect.y += 250 * dt
        # movement speed 250px/s

    new = self.rect
    for cell in pygame.sprite.spritecollide(self, game.walls, False):
      # Walls colissions
      # False == destroying touched object
      # RIGHT WALL COLLIDS FROM RIGHT
      # KEEPS PLAYER OUTSIDE OF THE WINDOW
      # WHICH IS BAD
      cell = cell.rect
      if last.right <= last.left and new.right > cell.left:
        new.right = cell.left
      if last.left >= cell.right and new.left < cell.right:
        new.left = cell.right
      if last.bottom <= cell.top and new.bottom > cell.top:
        new.bottom = cell.top
      if last.top >= cell.bottom and new.top < cell.bottom:
        new.top = cell.bottom

class Game(object):
  def main(self, screen):
    clock = pygame.time.Clock()

    background = pygame.image.load('background.png')
    sprites = pygame.sprite.Group()
    self.player = Player(sprites)

    self.walls = pygame.sprite.Group()
    block = pygame.image.load('block.png')
    for x in range(0, 640, 10):
      for y in range(0, 400, 10):
        if x in (0, 640-10) or y in (0, 400-10):
          wall = pygame.sprite.Sprite(self.walls)
          wall.image = block
          wall.rect = pygame.rect.Rect((x, y), block.get_size()) 
    sprites.add(self.walls)

    while 1:
      dt = clock.tick(30)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
          return


      sprites.update(dt / 1000., self)
      screen.blit(background, (0, 0))
      sprites.draw(screen)
      pygame.display.flip()

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640, 400))
  Game().main(screen)

