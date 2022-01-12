import pygame as pg
import random as rd
import config
import assets
import arrow

# Instâncias
arConfig = config.ArrowConfig()
wdConfig = config.WindowConfig()
clock = pg.time.Clock()

# arrow = arrow.Arrow()
assets = assets.Assets(0, (arConfig.pressed_arrow_size, arConfig.pressed_arrow_size))
assets.load()

pg.init()

pg.display.set_caption(wdConfig.window_title)
pg.display.set_icon(wdConfig.icon)

arrows_array = []
direction_list = ['left', 'up', 'down', 'right']

window = pg.display.set_mode((wdConfig.window_width, wdConfig.window_height))
window_open = True
while window_open:

    window.blit(wdConfig.background_image, (0, 0)),
    window.blit(assets.static_arrows['left'], (arConfig.static_arrows_x_position['left'], arConfig.static_arrows_y_position)),
    window.blit(assets.static_arrows['up'], (arConfig.static_arrows_x_position['up'], arConfig.static_arrows_y_position)),
    window.blit(assets.static_arrows['down'], (arConfig.static_arrows_x_position['down'], arConfig.static_arrows_y_position)),
    window.blit(assets.static_arrows['right'], (arConfig.static_arrows_x_position['right'], arConfig.static_arrows_y_position))

    pressed = pg.key.get_pressed()

    # Mantem a janela aberta
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window_open = False

        # Desliga a tela apertando ESC
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            window_open = False

    if pressed[pg.K_LEFT]:
        window.blit(assets.pressed_arrows['left'],
                    (arConfig.pressed_arrows_x_position['left'], arConfig.pressed_arrows_y_position))

    if pressed[pg.K_UP]:
        window.blit(assets.pressed_arrows['up'],
                    (arConfig.pressed_arrows_x_position['up'], arConfig.pressed_arrows_y_position))

    if pressed[pg.K_DOWN]:
        window.blit(assets.pressed_arrows['down'],
                    (arConfig.pressed_arrows_x_position['down'], arConfig.pressed_arrows_y_position))

    if pressed[pg.K_RIGHT]:
        window.blit(assets.pressed_arrows['right'],
                    (arConfig.pressed_arrows_x_position['right'], arConfig.pressed_arrows_y_position))

    '''
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                window.blit(assets.pressed_arrows['left'],
                            (arConfig.static_arrows_x_position['left'], arConfig.static_arrows_y_position))

            if event.key == pg.K_UP:
                window.blit(assets.pressed_arrows['up'],
                            (arConfig.static_arrows_x_position['up'], arConfig.static_arrows_y_position))

            if event.key == pg.K_DOWN:
                window.blit(assets.pressed_arrows['down'],
                            (arConfig.static_arrows_x_position['down'], arConfig.static_arrows_y_position))

            if event.key == pg.K_RIGHT:
                window.blit(assets.pressed_arrows['right'],
                            (arConfig.static_arrows_x_position['right'], arConfig.static_arrows_y_position))'''



    # Adiciona setas no array aleatoriamente
    random_ratio = rd.uniform(0, 20 - arConfig.difficult)
    if random_ratio <= 1 and len(arrows_array) <= arConfig.max_arrows:
        arrows_array.append(arrow.Arrow(rd.choice(direction_list), arConfig.arrow_falling_speed))

    # Atualiza e Desenha na tela
    for i in range(len(arrows_array)):
        arrows_array[i].update()
        arrows_array[i].draw()

    arrows_array = [x for x in arrows_array if not x.isOutOfBounds()]
    clock.tick(wdConfig.fps)
    pg.display.update()

pg.quit()
