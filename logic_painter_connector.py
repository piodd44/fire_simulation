from sim_logic import SimLogic
from painter import Painter
import vector_calculator

RED = [200, 0, 0]
BLUE = [0, 200, 0]
YELlOW = [0, 0, 200]


class LogicPainterConnector:
    def __init__(self, painter: Painter, sim_logic: SimLogic, box_size=25):
        self.box_size = box_size
        self.painter = painter
        self.sim_logic = sim_logic

    def draw_sim_map(self, line_width=4):
        box_size = self.box_size
        painter = self.painter
        sim_logic = self.sim_logic
        game_map = sim_logic.sim_map
        for x, line in enumerate(game_map):
            for y, value in enumerate(line):
                if value == 1:
                    painter.draw_rect(pos_vector=[x * box_size, y * box_size], color=RED,
                                      size=(box_size - line_width, box_size - line_width))
                if value == 0:
                    painter.draw_rect(pos_vector=[x * box_size, y * box_size], color=BLUE,
                                      size=(box_size - line_width, box_size - line_width))

    def input_mouse_input(self, mouse_input: [bool], mouse_pos: [float]):
        # print(mouse_input)
        map_pos = vector_calculator.rescale_pos(mouse_pos, scale=1 / self.box_size)
        self.sim_logic.input_mouse_input(mouse_input=mouse_input, map_pos=map_pos)
