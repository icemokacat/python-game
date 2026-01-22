import os
import pygame
from objects.fighter import Fighter
from objects.alien import Alien

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
# fighter_image = pygame.image.load(fighter_image_path)

fighter = Fighter(fighter_image_path, window_x, window_y)

alien_image_name = "alien1.png"
alien_image_path = os.path.join(PROJECT_ROOT, "assets", "images", alien_image_name)

# 여러 외계인 리스트
aliens = []
for y in range(5):
    for x in range(10):
        alien_instance = Alien(alien_image_path)
        alien_instance.x = 70 + x * 50
        alien_instance.y = 100 + y * 70
        aliens.append(alien_instance)

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
    #surface.blit(fighter.image, (fighter.x, fighter.y))
    fighter.draw(surface)
    # alien 초기 위치에 그리기
    # surface.blit(scale_up_alien_image, (init_alien_x, init_alien_y))
    for alien in aliens:
        alien.draw(surface)
    # 그리고 업데이트 (반영)
    pygame.display.update()
    # 프레임률 설정
    clock.tick(30)