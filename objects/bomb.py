from objects.object import Object

class Bomb(Object):
    def __init__(self, x, y):
        # 이미지 로드
        super().__init__("bomb.png")
        self.x = x
        self.y = y

        self.speed = 200
        self.direction_y = 1  # 아래로 이동