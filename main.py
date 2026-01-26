import pygame

from objects.beam import Beam
from objects.fighter import Fighter
from objects.alien import Alien
from objects.explosion import Explosion
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
fighter = Fighter()
beam = None

# 여러 외계인 리스트
aliens = []
for y in range(4):
    for x in range(5):
        alien_instance = Alien()
        alien_instance.x = 100 + x * 50
        alien_instance.y = 60 + y * 70
        aliens.append(alien_instance)

bombs = []
explosions = []

# 게임 루프
while True:

    ### Render ###

    # 배경을 검정색으로 칠함
    surface.fill((0, 0, 0))
    fighter.draw(surface)
    # beam 이 존재하면 그리기
    if beam is not None:
        beam.draw(surface)

    # 모든 외계인 그리기
    for alien in aliens:
        alien.draw(surface)

        bomb = alien.shoot()
        if bomb is not None:
            bombs.append(bomb)

    # 모든 bombs 그리기
    for bomb in bombs:
        bomb.draw(surface)

    # 모든 explosions 그리기
    for explosion in explosions:
        explosion.draw(surface)

    direction = 0
    # print("Update")

    ### 이벤트 처리 부분 ###

    for event in pygame.event.get():
        # 종료 이벤트 처리
        if (event.type == pygame.QUIT or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            print("Shutdown")
            pygame.quit()
            exit()
            break
        # 키보드  이벤트 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter.direction_x = -1
            elif event.key == pygame.K_RIGHT:
                fighter.direction_x = 1
            elif event.key == pygame.K_z:
                if beam is None:
                    beam = Beam( fighter.x + fighter.image.get_width() / 2 , fighter.y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighter.direction_x = 0

    ### Update ###

    # 프레임률 설정
    delta_seconds = clock.tick(FPS) / 1000
    # 이동
    fighter.update(delta_seconds)

    # 모든 외계인 이동
    for alien in aliens:
        alien.update(delta_seconds)

    # bombs 투척
    for bomb in bombs:
        bomb.update(delta_seconds)
        # 화면 밖으로 나가면 제거
        if SCREEN_HEIGHT < bomb.y:
            bombs.remove(bomb)
        else:
            if bomb.check_collision([fighter]) is not None:
                explosions.append(Explosion(fighter.rect))
                bombs.remove(bomb)
                print("Game Over")
                break

    # explosions 업데이트
    for explosion in explosions:
        explosion.update(delta_seconds)
        if explosion.is_finished():
            explosions.remove(explosion)

    # beam 이 존재하면 업데이트
    if beam is not None:
        beam.update(delta_seconds)
        if beam.y < 0:
            # 화면 밖으로 나가면 beam 제거
            beam = None
        else:
            dead_alien = beam.check_collision(aliens)
            if dead_alien is not None:
                explosions.append(Explosion(dead_alien.rect))
                aliens.remove(dead_alien)
                beam = None

    # 방향 전환이 필요한 경우
    if Alien.should_change_direction:
        Alien.should_change_direction = False

        for alien in aliens:
            # 반대로
            alien.direction_x *= -1
            # 아래로 약간 이동
            alien.move(0, 50)

    # 그리고 업데이트 (반영)
    pygame.display.update()
