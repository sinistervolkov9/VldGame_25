import pygame as pg
from settings import SCREEN_POS


class Markup:
    def __init__(self, game):
        self.game = game

    def draw(self,):
        for pos in SCREEN_POS.values():
            pg.draw.circle(self.game.screen, "red", pos, 5)
