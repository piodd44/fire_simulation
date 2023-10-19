import random

import vector_calculator
import map_saver

MAP_1 = [[0, 1, 1, 1, 1],
         [0, 1, 1, 0, 1],
         [0, 1, 0, 1, 1]
    , [0, 1, 0, 1, 0]
    , [0, 1, 1, 1, 1]]
X, Y = 50, 50
MAP_2 = [[0 for x in range(X)] for y in range(Y)]


class SimLogic:
    def __init__(self, map_size: [int], game_map=MAP_2, box_size=50):
        self.map_size = map_size
        self.sim_map = game_map
        self.box_size = box_size

    def get_map(self):
        return self.sim_map

    def input_mouse_input(self, mouse_input, map_pos):
        left_click = mouse_input[0]
        if left_click:
            try:
                print("klikniete")
                print(map_pos)
                self.sim_map[map_pos[0]][map_pos[1]] = (self.sim_map[map_pos[0]][map_pos[1]] + 1) % 2
            except IndexError as e:
                pass

    def make_action(self, inpute_key):
        print(inpute_key)
        if inpute_key == "s":
            print("zapisuje_mape")
            path = "game_maps/test_map_1.txt"
            map_saver.save_map(self.sim_map, file_path=path)

    def sim_iteration(self):
        for x, line in enumerate(self.sim_map):
            for y, value in enumerate(line):
                if value == 1:
                    self.spreed_from(x, y)

    def spreed_from(self, x, y):
        sim_map = self.sim_map
        p_fire_spreed = 0.01
        if x > 0:
            if random.random() < p_fire_spreed:
                sim_map[x - 1][y] = 1
        if y > 0:
            if random.random() < p_fire_spreed:
                sim_map[x][y - 1] = 1
        if x + 1 < len(sim_map):
            if random.random() < p_fire_spreed:
                sim_map[x + 1][y] = 1
        if y + 1 < len(sim_map[0]):
            if random.random() < p_fire_spreed:
                sim_map[x][y + 1] = 1
