import pygame as pg
import config

arConfig = config.ArrowConfig


class Assets:

    def __init__(self, arrow_size: (int, int), pressed_arrow_size: (int, int)):
        self.arrow_size = arrow_size
        self.pressed_arrow_size = pressed_arrow_size
        if arrow_size == 0:
            self.arrow_size = (arConfig.max_arrow_scale, arConfig.max_arrow_scale)

        # self.static_arrow_size = (50, 50)

        self.arrows = []
        self.static_arrows = []
        self.pressed_arrows = []

    def load(self):
        self.arrows = {'left': pg.transform.scale(pg.image.load(arConfig.arrow_images['left']), self.arrow_size),
                       'up': pg.transform.scale(pg.image.load(arConfig.arrow_images['up']), self.arrow_size),
                       'down': pg.transform.scale(pg.image.load(arConfig.arrow_images['down']), self.arrow_size),
                       'right': pg.transform.scale(pg.image.load(arConfig.arrow_images['right']), self.arrow_size)}

        self.static_arrows = {
            'left': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['left']), self.arrow_size),
            'up': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['up']), self.arrow_size),
            'down': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['down']), self.arrow_size),
            'right': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['right']), self.arrow_size)}

        self.pressed_arrows = {
            'left': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['left']), self.pressed_arrow_size),
            'up': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['up']), self.pressed_arrow_size),
            'down': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['down']), self.pressed_arrow_size),
            'right': pg.transform.scale(pg.image.load(arConfig.static_arrow_images['right']), self.pressed_arrow_size)}
