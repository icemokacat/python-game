from constants import SCREEN_WIDTH
from objects.object import Object

class Bunker(Object):
    def __init__(self, fighter):
        # Super Class 인 Object 클래스를 호출
        super().__init__("bunker.png")

        # 초기 위치 설정
        self.x = fighter.x - (self.image.get_width() / 2) + (fighter.image.get_width() / 2)
        self.y = fighter.y - self.image.get_height() - 10
        self.direction_y = 0
        self.speed = fighter.speed
        self.direction_x = fighter.direction_x

        self.protect_count = 10

    def damage(self):
        self.protect_count -= 1

    def is_destroyed(self):
        return self.protect_count <= 0