import pygame
import objects.assetUtils as assetUtils
from objects.fighter import Fighter
from objects.alien import Alien
from constants import *

print("Startup")

# pygame setup
pygame.init()
# enable key repeat for held keys
pygame.key.set_repeat(500, 500)
# create window
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set frame rate init
# 이후 게임 루프에서 매 프레임마다 clock.tick(프레임률) 호출 필요
clock = pygame.time.Clock()

# image setup
fighter = Fighter(assetUtils.get_asset_image_path("fighter.png"))

# 여러 외계인 리스트
aliens = []
for y in range(8):
    for x in range(5):
        alien_instance = Alien(assetUtils.get_asset_image_path("alien1.png"))
        alien_instance.x = 100 + x * 50
        alien_instance.y = 60 + y * 70
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
    clock.tick(FPS)