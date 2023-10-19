import random
import time

import vector_calculator
import map_saver

MAP_1 = [[0, 1, 1, 1, 1],
         [0, 1, 1, 0, 1],
         [0, 1, 0, 1, 1]
    , [0, 1, 0, 1, 0]
    , [0, 1, 1, 1, 1]]
X, Y = 55, 55
MAP_2 = [[0 for x in range(X)] for y in range(Y)]
NEXT_MAP = [[0 for x in range(X)] for y in range(Y)]
WATER_VALUE = 2


class SimLogic:
    def __init__(self, map_size: [int], game_map=MAP_2, box_size=50, p_fired_spreed=0.1):
        self.p_fire_spreed = p_fired_spreed
        self.map_size = map_size
        self.sim_map = game_map
        self.box_size = box_size
        self.next_map = NEXT_MAP

    def get_map(self):
        return self.sim_map

    def input_mouse_input(self, mouse_input, map_pos):
        left_click = mouse_input[0]
        right_click = mouse_input[-2]
        if left_click:
            try:
                self.sim_map[map_pos[0]][map_pos[1]] = (self.sim_map[map_pos[0]][map_pos[1]] + 1) % 2
                self.next_map[map_pos[0]][map_pos[1]] = (self.next_map[map_pos[0]][map_pos[1]] + 1) % 2
            except IndexError as e:
                pass
        if right_click:
            try:
                self.sim_map[map_pos[0]][map_pos[1]] = 2
                self.next_map[map_pos[0]][map_pos[1]] = 2
            except IndexError as e:
                pass

    def make_action(self, inpute_key):
        print(inpute_key)
        if inpute_key == "l":
            print("zapisuje_mape")
            path = "sim_maps/test_map_1.txt"
            map_saver.save_map(self.sim_map, file_path=path)

    def sim_iteration(self):
        start_time = time.time()
        for x, line in enumerate(self.sim_map):
            for y, value in enumerate(line):
                if value == 1:
                    self.spreed_from(x, y)
        for x in range(len(self.sim_map)):
            for y in range(len(self.sim_map[0])):
                self.sim_map[x][y] = NEXT_MAP[x][y]
        end_time = time.time()

    # print("one iteration time == ", end_time - start_time)

    def spreed_from(self, x, y):
        sim_map = self.sim_map
        next_map = self.next_map
        p_fire_spreed = self.p_fire_spreed
        if x > 0:
            if random.random() < p_fire_spreed and sim_map[x - 1][y] != WATER_VALUE:
                next_map[x - 1][y] = 1
        if y > 0:
            if random.random() < p_fire_spreed and sim_map[x][y - 1] != WATER_VALUE:
                next_map[x][y - 1] = 1
        if x + 1 < len(sim_map):
            if random.random() < p_fire_spreed and sim_map[x + 1][y] != WATER_VALUE:
                next_map[x + 1][y] = 1
        if y + 1 < len(sim_map[0]):
            if random.random() < p_fire_spreed and sim_map[x][y + 1] != WATER_VALUE:
                next_map[x][y + 1] = 1

    def save_map(self):
        path = "sim_maps/test_map_1.txt"
        map_saver.save_map(self.sim_map, file_path=path)
