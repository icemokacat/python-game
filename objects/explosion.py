from objects.object import Object

class Explosion(Object):
    def __init__(self, rect):
        super().__init__("explosion.png")

        # 폭발 위치를 rect 중앙에 맞춤
        self.x = rect.center[0] - self.rect.center[0]
        self.y = rect.center[1] - self.rect.center[1]

        # 폭발 지속 시간 (초)
        self.duration = 1.0

    def update(self, delta_seconds):
        super().update(delta_seconds)
        self.duration -= delta_seconds

    def is_finished(self):
        return self.duration <= 0

