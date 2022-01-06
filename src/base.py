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
assets = assets.Assets(0)
assets.load()

pg.init()

pg.display.set_caption(wdConfig.window_title)
pg.display.set_icon(wdConfig.icon)

arrows_array = []
direction_list = ['left', 'up', 'down', 'right']

window = pg.display.set_mode((wdConfig.window_width, wdConfig.window_height))
window_open = True
while window_open:

    window.blit(wdConfig.background_image, (0, 0))
    window.blit(assets.static_arrows['left'], (arConfig.static_arrows_x_position['left'], arConfig.static_arrows_y_position))
    window.blit(assets.static_arrows['up'], (arConfig.static_arrows_x_position['up'], arConfig.static_arrows_y_position))
    window.blit(assets.static_arrows['down'], (arConfig.static_arrows_x_position['down'], arConfig.static_arrows_y_position))
    window.blit(assets.static_arrows['right'], (arConfig.static_arrows_x_position['right'], arConfig.static_arrows_y_position))

    # Mantem a janela aberta
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window_open = False

    # Executa os botões
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window_open = False

    # Adiciona setas no array aleatoriamente
    if rd.random() * 10 <= 1 and len(arrows_array) <= arConfig.max_arrows:
        arrows_array.append(arrow.Arrow(rd.choice(direction_list), arConfig.arrow_falling_speed))

    # Atualiza e Desenha na tela
    for i in range(len(arrows_array)):
        arrows_array[i].update()
        arrows_array[i].draw()

    arrows_array = [x for x in arrows_array if not x.isOutOfBounds()]
    clock.tick(wdConfig.fps)
    pg.display.update()

pg.quit()
