import pygame as pg
import config
import assets

arConfig = config.ArrowConfig()
wdConfig = config.WindowConfig()

assets = assets.Assets(0, (arConfig.pressed_arrow_size, arConfig.pressed_arrow_size))
assets.load()

window = pg.display.set_mode((wdConfig.window_width, wdConfig.window_height))


class Arrow:

    def __init__(self, direction: str, speed: float):
        self.direction = direction
        self.speed = speed
        self.y_position = -1 * arConfig.max_arrow_scale

        self.draw()

    def isOutOfBounds(self):
        return self.y_position >= wdConfig.window_height

    def draw(self):

        if self.y_position < 100:
            arrow_scaling = (arConfig.min_arrow_scale, arConfig.min_arrow_scale)

        elif 100 <= self.y_position <= 400:
            arrow_scaling = ((self.y_position / 4), (self.y_position / 4))

        else:
            arrow_scaling = (arConfig.max_arrow_scale, arConfig.max_arrow_scale)

        if self.direction == 'left':
            x_initial_position = arConfig.arrow_x_initial['left']
            x_position = x_initial_position - (arrow_scaling[0]/2)
            window.blit(pg.transform.scale(assets.arrows['left'], arrow_scaling), (x_position, self.y_position))

        elif self.direction == 'up':
            x_initial_position = arConfig.arrow_x_initial['up']
            x_position = x_initial_position - (arrow_scaling[0]/2)
            window.blit(pg.transform.scale(assets.arrows['up'], arrow_scaling), (x_position, self.y_position))

        elif self.direction == 'down':
            x_initial_position = arConfig.arrow_x_initial['down']
            x_position = x_initial_position - (arrow_scaling[0]/2)
            window.blit(pg.transform.scale(assets.arrows['down'], arrow_scaling), (x_position, self.y_position))

        elif self.direction == 'right':
            x_initial_position = arConfig.arrow_x_initial['right']
            x_position = x_initial_position - (arrow_scaling[0]/2)
            window.blit(pg.transform.scale(assets.arrows['right'], arrow_scaling), (x_position, self.y_position))

    def update(self):
        self.y_position += self.speed
