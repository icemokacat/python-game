import pygame

class Object:
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
        self.speed = 200
        self.direction = 0

    def draw(self, _surface):
        _surface.blit(self.image, (self.x, self.y))

    def update(self, delta_seconds):
        self.move(self.direction * self.speed * delta_seconds, 0)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
