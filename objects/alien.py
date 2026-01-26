from constants import SCREEN_WIDTH
from objects.object import Object
from objects.bomb import Bomb
import random

class Alien(Object):
    should_change_direction = False
    def __init__(self):
        # 이미지 로드
        super().__init__("alien1.png")
        self.speed = 100
        self.direction_x = 1

    def update(self, delta_seconds):
        super().update(delta_seconds)

        right = self.x + self.image.get_width()

        if SCREEN_WIDTH <= right:
            # 화면 오른쪽 끝에 닿음
            Alien.should_change_direction = True
        if self.x <= 0:
            # 화면 왼쪽 끝에 닿음
            Alien.should_change_direction = True

    def shoot(self):
        if random.random() < 0.005:
            return Bomb(self.x + self.image.get_width()/2 , self.y + self.image.get_height())
        return None