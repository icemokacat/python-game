from constants import *
from objects.object import Object

class Fighter(Object):
    def __init__(self, image_path):
        # Super Class 인 Object 클래스를 호출
        super().__init__(image_path)
        # 초기 위치 설정
        self.x = SCREEN_WIDTH / 2 - self.image.get_width() / 2
        self.y = SCREEN_HEIGHT - self.image.get_height() - 20

