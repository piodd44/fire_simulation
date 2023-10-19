import time

import pygame
from painter import Painter
from event_listener import EventListener
from sim_logic import SimLogic
from logic_painter_connector import LogicPainterConnector

HEIGHT = 1920
WIDTH = 1020
pygame.init()

screen = pygame.display.set_mode((HEIGHT, WIDTH))
BOX_SIZE = 15
clock = pygame.time.Clock()
painter = Painter(screen=screen)
event_listener = EventListener()
sim_logic = SimLogic(map_size=[10, 10], box_size=BOX_SIZE)
logic_painter_connector = LogicPainterConnector(painter=painter, sim_logic=sim_logic, box_size=BOX_SIZE)


def calculate_map_pos(pos_vector: [int]):
    return pos_vector


def blank():
    pass


object_to_draw_list_size = 20000
object_to_draw_list = [(blank, ()) for x in range(object_to_draw_list_size)]
object_to_draw_index = 0

while True:
    start_time = time.time()
    object_to_draw_index = (object_to_draw_index + 1) % object_to_draw_list_size
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...
    painter.clear()
    # painter.draw_circle(pos_vector=[x, 100], color=BLUE, radius=100)
    # painter.draw_rect(pos_vector=[x, 200], color=RED, size=[10, 10])
    # painter.draw_cris_cross(box_size=25, color=YELlOW, pos_vector=[0, 0], size=[25, 25])

    mouse_pos = event_listener.get_mouse_pos()
    # print(mouse_pos)
    get_presed = event_listener.get_mouse_pressed()

    logic_painter_connector.input_mouse_input(mouse_input=get_presed, mouse_pos=mouse_pos)
    logic_painter_connector.draw_sim_map()

    inpute_list = event_listener.get_key_pressed()

    sim_logic.sim_iteration()

    for inpute_key in inpute_list:
        logic_painter_connector.input_key(input_key=inpute_key)
        # sim_logic.make_action(inpute_key)
    pygame.display.flip()  # Refresh on-screen display

    clock.tick(60)  # wait until next frame (at 60 FPS)
    end_time = time.time()
    # print(end_time - start_time)
