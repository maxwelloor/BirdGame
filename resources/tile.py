import pygame

class Tile:

    def __init__(self, x, y, tile_list):
        self.x = x
        self.y = y

        self.set_img()

        tile_list.append(self)

    def set_img(self):
        self.img = None

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))


class Brick_Tile(Tile):

    def set_img(self):
        self.img = pygame.image.load('sprites\\Brick_Tile.png')

