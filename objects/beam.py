from objects.object import Object

class Beam(Object):
    def __init__(self, image_path, x, y):
        # 이미지 로드
        super().__init__(image_path)
        self.x = x
        self.y = y

        self.speed = 600
        self.direction_y = -1  # 위로 이동
