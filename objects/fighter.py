import pygame
from constants import *
class Fighter:
    def __init__(self, image_path):
        # 이미지 로드
        origin_image = pygame.image.load(image_path)
        # 이미지 크기 조정 (옵션)
        self.image = pygame.transform.scale(
            origin_image,
            (origin_image.get_width() * 2, origin_image.get_height() * 2)
        )
        # 초기 위치 설정
        self.x = SCREEN_WIDTH / 2 - self.image.get_width() / 2
        self.y = SCREEN_HEIGHT - self.image.get_height() - 20
        self.speed = 200
        self.direction = 0

    def draw(self, _surface):
        _surface.blit(self.image, (self.x, self.y))

    def move(self, delta_seconds):
        self.x = self.x + self.direction * self.speed * delta_seconds
