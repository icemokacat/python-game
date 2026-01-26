from constants import SCREEN_WIDTH
from objects.object import Object

class Alien(Object):
    should_change_direction = False
    def __init__(self, image_path):
        # 이미지 로드
        super().__init__(image_path)
        self.speed = 100
        self.direction = 1

    def update(self, delta_seconds):
        super().update(delta_seconds)

        right = self.x + self.image.get_width()

        if SCREEN_WIDTH <= right:
            # 화면 오른쪽 끝에 닿음
            Alien.should_change_direction = True
        if self.x <= 0:
            # 화면 왼쪽 끝에 닿음
            Alien.should_change_direction = True