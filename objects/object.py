import pygame
import utils.assetUtils as assetUtils

class Object:
    def __init__(self, image_name):
        # 이미지 로드
        origin_image = pygame.image.load(assetUtils.get_asset_image_path(image_name))
        # 이미지 크기 조정 (옵션)
        self.image = pygame.transform.scale(
            origin_image,
            (origin_image.get_width() * 2, origin_image.get_height() * 2)
        )
        # 초기 위치 설정
        self.x = 0
        self.y = 0
        self.speed = 200
        self.direction_x = 0
        self.direction_y = 0

    def draw(self, _surface):
        _surface.blit(self.image, (self.x, self.y))

    def update(self, delta_seconds):
        self.move(self.direction_x * self.speed * delta_seconds,
                  self.direction_y * self.speed * delta_seconds)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
