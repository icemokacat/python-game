import pygame

from constants import *
from scenes.base_scene import BaseScene
from scenes.scene_manager import SceneManager

class GameClearScene(BaseScene):
    def __init__(self):
        pass

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Clear !!", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))
        surface.blit(text, text_rect)

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change(HOME_SCENE_NAME)