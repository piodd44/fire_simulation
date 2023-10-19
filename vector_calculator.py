def add_to_vector_1(vector_1: [int], vector_2: [int]):
    vector_1[0] += vector_2[0]
    vector_1[1] += vector_2[1]


def add_to_vectors(vector_1: [int], vector_2: [int]):
    x = vector_1[0] + vector_2[0]
    y = vector_1[1] + vector_2[1]
    return [x, y]


def rescale_pos(vector: [int], scale: float):
    return [int(vector[0] * scale), int(vector[1] * scale)]
