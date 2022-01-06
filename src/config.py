import pygame as pg


class ArrowConfig:
    arrow_x_initial = {'left': 100,
                       'up': 300,
                       'down': 500,
                       'right': 700}

    static_arrows_x_position = {'left': 50,
                                'up': 250,
                                'down': 450,
                                'right': 650}

    static_arrows_y_position = 400

    static_arrow_images = {'left': 'img/static_arrow_left.png',
                           'up': 'img/static_arrow_up.png',
                           'down': 'img/static_arrow_down.png',
                           'right': 'img/static_arrow_right.png'}

    arrow_images = {'left': 'img/arrow_left.png',
                    'up': 'img/arrow_up.png',
                    'down': 'img/arrow_down.png',
                    'right': 'img/arrow_right.png'}

    max_arrow_scale = 100
    min_arrow_scale = 25
    max_arrows = 50
    arrow_falling_speed = 8


class WindowConfig:
    window_width = 800
    window_height = 600
    window_title = 'Guitar Harrow'
    icon = pg.image.load('img/arrow_down.png')
    fps = 30
    background_image = pg.image.load('img/background_lost_in_mind.jpg')
