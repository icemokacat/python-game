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
window_x = 640
window_y = 480
surface = pygame.display.set_mode((window_x, window_y))
# set frame rate init
# 이후 게임 루프에서 매 프레임마다 clock.tick(프레임률) 호출 필요
clock = pygame.time.Clock()

# image setup
fighter_image_name = "fighter.png"
fighter_image_path = os.path.join(PROJECT_ROOT, "assets", "images", fighter_image_name)
fighter_image = pygame.image.load(fighter_image_path)

alien_image_name = "alien1.png"
alien_image_path = os.path.join(PROJECT_ROOT, "assets", "images", alien_image_name)
alien_image = pygame.image.load(alien_image_path)

# 이미지 크기 조정 (옵션)
# 파이터
origin_image_width = fighter_image.get_width()
origin_image_height = fighter_image.get_height()
scale_up_image = pygame.transform.scale(
    fighter_image,
    (origin_image_width * 2, origin_image_height * 2)
)
# 외계인
origin_alien_width = alien_image.get_width()
origin_alien_height = alien_image.get_height()
scale_up_alien_image = pygame.transform.scale(
    alien_image,
    (origin_alien_width * 2, origin_alien_height * 2)
)

# 파이터 초기 위치
init_x = window_x / 2 - scale_up_image.get_width() / 2
init_y = window_y - scale_up_image.get_height() - 20

# 외계인 초기 위치
init_alien_x = 70
init_alien_y = 100

# 여러 외계인 위치 리스트
alien_pos = []
for i in range(4):
    for j in range(3):
        alien_pos.append( (init_alien_x + 50*i, init_alien_y + 70*j) )

# 게임 루프
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
    # fighter 초기 위치에 그리기
    surface.blit(scale_up_image, (init_x, init_y))
    # alien 초기 위치에 그리기
    # surface.blit(scale_up_alien_image, (init_alien_x, init_alien_y))
    for pos in alien_pos:
        surface.blit(scale_up_alien_image, pos)
    # 그리고 업데이트 (반영)
    pygame.display.update()
    # 프레임률 설정
    clock.tick(30)