import pygame

from constants import *
from scenes.game_clear_scene import GameClearScene
from scenes.game_over_scene import GameOverScene
from scenes.game_scene import GameScene
from scenes.home_scene import HomeScene
from scenes.scene_manager import SceneManager

print("Startup")

# pygame 초기화 함수
def pygame_init():
    # pygame setup
    pygame.init()
    # enable key repeat for held keys
    pygame.key.set_repeat(100, 200)

pygame_init()
# create window
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set frame rate init
# 이후 게임 루프에서 매 프레임마다 clock.tick(프레임률) 호출 필요
clock = pygame.time.Clock()

## scene setup ##
SceneManager.instance.add(HOME_SCENE_NAME       , HomeScene())
SceneManager.instance.add(GAME_SCENE_NAME       , GameScene())
SceneManager.instance.add(GAME_OVER_SCENE_NAME  , GameOverScene())
SceneManager.instance.add(GAME_CLEAR_SCENE_NAME , GameClearScene())

# 게임 루프
while True:

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
            SceneManager.instance.scene.on_key_down(event.key)
        if event.type == pygame.KEYUP:
            SceneManager.instance.scene.on_key_up(event.key)

    # 프레임률 설정
    delta_seconds = clock.tick(FPS) / 1000
    ### Update ###
    SceneManager.instance.scene.on_update(delta_seconds)

    ### Render ###
    # 배경을 검정색으로 칠함
    surface.fill((0, 0, 0))
    SceneManager.instance.scene.on_render(surface)

    # 그리고 업데이트 (반영)
    pygame.display.update()


