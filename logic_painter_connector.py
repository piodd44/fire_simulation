from sim_logic import SimLogic
from painter import Painter
import vector_calculator

GREEN = [0, 200, 0]
BLUE = [0, 222, 222]
YELlOW = [0, 0, 200]
RED = [200, 0, 0]


class Camera:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class LogicPainterConnector:
    def __init__(self, painter: Painter, sim_logic: SimLogic, box_size=25):
        self.box_size = box_size
        self.painter = painter
        self.sim_logic = sim_logic
        self.camera = Camera(pos_x=0, pos_y=0)

    def draw_sim_map(self, line_width=4):
        box_size = self.box_size
        painter = self.painter
        sim_logic = self.sim_logic
        game_map = sim_logic.sim_map
        min_x, max_x, min_y, max_y = self.calculate_field_of_view(sim_map=game_map)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                value = game_map[x][y]
                pos_vector = [x * box_size - self.camera.pos_x, y * box_size - self.camera.pos_y]
                if value == 0:
                    painter.draw_rect(pos_vector=pos_vector, color=GREEN,
                                      size=(box_size - line_width, box_size - line_width))
                if value == 1:
                    painter.draw_rect(pos_vector=pos_vector, color=RED,
                                      size=(box_size - line_width, box_size - line_width))
                if value == 2:
                    painter.draw_rect(pos_vector=pos_vector, color=BLUE,
                                      size=(box_size - line_width, box_size - line_width))

    def calculate_field_of_view(self, sim_map):
        field_of_view = 1200
        min_x = max((self.camera.pos_x - field_of_view) // self.box_size, 0)
        max_x = min((self.camera.pos_x + field_of_view) // self.box_size, len(sim_map))
        min_y = max((self.camera.pos_y - field_of_view) // self.box_size, 0)
        max_y = min((self.camera.pos_y + field_of_view) // self.box_size, len(sim_map[0]))
        return min_x, max_x, min_y, max_y

    def input_mouse_input(self, mouse_input: [bool], mouse_pos: [float]):
        # print(mouse_input)
        map_pos = vector_calculator.rescale_pos(mouse_pos, scale=1 / self.box_size)
        self.sim_logic.input_mouse_input(mouse_input=mouse_input, map_pos=map_pos)

    def input_key(self, input_key):
        print("w connector")
        print(input_key)
        if input_key == "s":
            self.camera.pos_y += 100
        elif input_key == "w":
            self.camera.pos_y -= 100
        elif input_key == "a":
            self.camera.pos_x -= 100
        elif input_key == "d":
            self.camera.pos_x += 100
        print(self.camera.pos_x, self.camera.pos_y)
        if input_key == "l":
            self.sim_logic.save_map()
