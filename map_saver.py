import pickle


def save_map(game_map: [[]], file_path):
    f = open(file_path, "wb")
    pickle.dump(game_map, f)
    f.close()


def load_map(file_path):
    file_path = "game_maps/map_1.txt"
    f = open(file_path, "rb")
    game_map = pickle.load(f)
    f.close()
    return game_map


#test_map = [
 #   [1, 1, 1],
#    [2, 2, 2],
#    [3, 3, 3]
#]
#test_file_path = "game_maps/map_1.txt"
#save_map(game_map=test_map, file_path=test_file_path)
#load_map(file_path=test_file_path)
