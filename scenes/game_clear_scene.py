import pygame

from constants import *
from scenes.base_scene import BaseScene
from scenes.scene_manager import SceneManager

class GameClearScene(BaseScene):

    def __init__(self):
        self.prev_scene_data = None
        self.score = 0

    def set_data(self, data):
        self.prev_scene_data = data

    def on_begin(self):
        print("GameClearScene: on_begin called")
        if self.prev_scene_data is not None:
            self.score = self.prev_scene_data.get('score', 0)
        else:
            print("No prev_scene_data")

    def on_end(self):
        print("GameClearScene: on_end called")
        self.prev_scene_data = None
        self.score = 0

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)

        text1 = font.render("Clear", True, (255, 255, 255))
        text2 = font.render("Your Score: {}".format(self.score), True, (255, 255, 255))
        text3 = font.render("Press Enter to Home", True, (255, 255, 255))

        text_height = text1.get_height()

        text1_rect = text1.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2 - text_height - 10))
        text2_rect = text2.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))
        text3_rect = text3.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2 + text_height + 10))

        #surface.blit(text, text_rect)
        surface.blit(text1, text1_rect)
        surface.blit(text2, text2_rect)
        surface.blit(text3, text3_rect)

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change(HOME_SCENE_NAME)