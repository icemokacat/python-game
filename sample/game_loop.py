import os
import pygame

print("Startup")

# setup paths for files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# pygame setup
pygame.init()
# enable key repeat for held keys
pygame.key.set_repeat(500, 500)
# create window
surface = pygame.display.set_mode((640, 480))
# set frame rate init
# 이후 게임 루프에서 매 프레임마다 clock.tick(프레임률) 호출 필요
clock = pygame.time.Clock()

# image setup
image_path = os.path.join(PROJECT_ROOT, "assets", "images", "fighter.png")
image = pygame.image.load(image_path)
# 이미지 크기 조정 (옵션)
origin_image_width = image.get_width()
origin_image_height = image.get_height()
scale_up_image = pygame.transform.scale(
    image,
    (origin_image_width * 10, origin_image_height * 10)
)

while True:

    print("Update")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shutdown")
            pygame.quit()
            exit()
            break

    print("Render")
    # 배경을 검정색으로 칠함
    surface.fill((0, 0, 0))
    # pygame.draw.rect(surface, (0, 255, 0), (10, 10, 100, 100))
    # blit 이란 말은 'block image transfer' 의 줄임말로,
    # 한 표면에서 다른 표면으로 이미지를 복사하는 것을 의미합니다.
    surface.blit(scale_up_image, (100, 200))
    # 그리고 업데이트 (반영)
    pygame.display.update()
    # 프레임률 설정
    clock.tick(30)