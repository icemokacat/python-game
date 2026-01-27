from objects.object import Object

class Ufo(Object):
    def __init__(self):
        # Super Class 인 Object 클래스를 호출
        super().__init__("ufo.png")
        # 초기 위치 설정
        self.x = 0
        self.y = self.image.get_height() + 20
        self.speed = 150
        self.direction_x = 1
