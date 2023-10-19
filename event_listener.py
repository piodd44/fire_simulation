import pygame


class EventListener:
    def __init__(self):
        self.last_mouse_click_state = [False, False, False]

    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

    def get_mouse_click(self):
        return pygame.mouse.get_pressed()

    def get_mouse_pressed(self):
        pressed = []
        new_state_list = self.get_mouse_click()
        for new_state in new_state_list:
            for old_state in self.last_mouse_click_state:
                pressed.append(new_state and old_state != new_state)
        self.last_mouse_click_state = new_state_list
        return pressed

    def get_key_pressed(self):
        input_key_list = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                input_key_list.append(event.unicode)
                print(event.unicode)
            if event.type == pygame.QUIT:
                exit(11)
        return input_key_list
