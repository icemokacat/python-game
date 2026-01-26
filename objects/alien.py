import pygame

from constants import SCREEN_WIDTH


class Alien:
    should_change_direction = False
    def __init__(self, image_path):
        # 이미지 로드
        origin_image = pygame.image.load(image_path)
        # 이미지 크기 조정 (옵션)
        self.image = pygame.transform.scale(
            origin_image,
            (origin_image.get_width() * 2, origin_image.get_height() * 2)
        )
        # 초기 위치 설정
        self.x = 0
        self.y = 0

        self.speed = 100
        self.direction = 1

    def draw(self, _surface):
        _surface.blit(self.image, (self.x, self.y))

    def move(self, delta_seconds):
        self.x = self.x + self.direction * self.speed * delta_seconds
        right = self.x + self.image.get_width()

        if SCREEN_WIDTH <= right:
            # 화면 오른쪽 끝에 닿음
            Alien.should_change_direction = True
        if self.x <= 0:
            # 화면 왼쪽 끝에 닿음
            Alien.should_change_direction = True