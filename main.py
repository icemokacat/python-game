import pygame
import objects.assetUtils as assetUtils
from objects.fighter import Fighter
from objects.alien import Alien
from constants import *

print("Startup")

# pygame setup
pygame.init()
# enable key repeat for held keys
pygame.key.set_repeat(100, 100)
# create window
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set frame rate init
# 이후 게임 루프에서 매 프레임마다 clock.tick(프레임률) 호출 필요
clock = pygame.time.Clock()

# image setup
fighter = Fighter(assetUtils.get_asset_image_path("fighter.png"))

# 여러 외계인 리스트
aliens = []
for y in range(4):
    for x in range(5):
        alien_instance = Alien(assetUtils.get_asset_image_path("alien1.png"))
        alien_instance.x = 100 + x * 50
        alien_instance.y = 60 + y * 70
        aliens.append(alien_instance)

# 게임 루프
while True:

    ### 고정적으로 (변동없이 계속 실행되는 부분 ###

    # 배경을 검정색으로 칠함
    surface.fill((0, 0, 0))
    fighter.draw(surface)

    # 모든 외계인 그리기
    for alien in aliens:
        alien.draw(surface)

    direction = 0
    # print("Update")

    ### 이벤트 처리 부분 ###

    for event in pygame.event.get():
        # 종료 이벤트 처리
        if event.type == pygame.QUIT:
            print("Shutdown")
            pygame.quit()
            exit()
            break
        # 키보드  이벤트 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter.direction = -1
            elif event.key == pygame.K_RIGHT:
                fighter.direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighter.direction = 0

    ### Render ###

    # 프레임률 설정
    delta_seconds = clock.tick(FPS) / 1000
    # 이동
    fighter.move(delta_seconds)

    # 모든 외계인 이동
    for alien in aliens:
        alien.move(delta_seconds)

    # 방향 전환이 필요한 경우
    if Alien.should_change_direction:
        Alien.should_change_direction = False

        for alien in aliens:
            # 반대로
            alien.direction *= -1
            # 아래로 약간 이동
            alien.y += 50

    # 그리고 업데이트 (반영)
    pygame.display.update()
