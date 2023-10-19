import pygame
import vector_calculator


class Painter:
    def __init__(self, screen):
        self.screen = screen

    def draw_circle(self, pos_vector: [int], color: [int], radius: int):
        pygame.draw.circle(surface=self.screen, color=color, radius=radius, center=pos_vector)

    def draw_rect(self, pos_vector: [int], color: [int], size: [int]):
        rect = pos_vector, size
        pygame.draw.rect(surface=self.screen, color=color, rect=rect)

    def draw_cris_cross(self, box_size: int, color, pos_vector: [int], size: [int], line_width=2):
        for x in range(size[0]):
            for y in range(size[1]):
                shift = [(box_size + line_width) * x, (box_size + line_width) * y]
                self.draw_rect(pos_vector=vector_calculator.add_to_vectors(pos_vector, shift), color=color,
                               size=[box_size, box_size])

    def clear(self):
        self.screen.fill("black")
