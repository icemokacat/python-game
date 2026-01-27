from constants import *
from objects.bunker import Bunker
from objects.object import Object

class Fighter(Object):
    def __init__(self):
        # Super Class 인 Object 클래스를 호출
        super().__init__("fighter.png")
        # 초기 위치 설정
        self.x = SCREEN_WIDTH / 2 - self.image.get_width() / 2
        self.y = SCREEN_HEIGHT - self.image.get_height() - 20
        self.is_protected = False
        self.bunker = None

    def set_bunker(self):
        self.is_protected = True
        self.bunker = Bunker(self)

    def get_bunker(self):
        return self.bunker

    def update(self, delta_seconds):
        super().update(delta_seconds)
        if self.bunker is not None:
            # 벙커가 있으면 파괴여부 체크 후 제거
            if self.bunker.is_destroyed():
                self.is_protected = False
                self.bunker = None
            # 계속 존재하면 벙커 위치 갱신
            else:
                self.bunker.x = self.x - (self.bunker.image.get_width() / 2) + (self.image.get_width() / 2) + 1
                self.bunker.update(delta_seconds)

    def draw(self, surface):
        super().draw(surface)
        # 벙커가 있으면 같이 그리기
        if self.bunker is not None:
            self.bunker.draw(surface)