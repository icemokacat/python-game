import pygame

from objects.beam import Beam
from objects.alien import Alien
from objects.fighter import Fighter
from objects.explosion import Explosion
from constants import *
from scenes.base_scene import BaseScene
from scenes.scene_manager import SceneManager
from utils.mixerContainer import MixerContainer

class GameScene(BaseScene):
    def __init__(self):
        # 비행기 세팅
        self.fighter    = None
        self.aliens     = []
        self.bombs      = []
        self.explosions = []
        self.beams      = []
        self.score      = 0

        # sound setup
        self.soundMixer = MixerContainer()

    def on_begin(self):
        print("GameScene: on_begin called")
        self.fighter = Fighter()
        for y in range(1):
            for x in range(1):
                alien_instance = Alien()
                alien_instance.x = 100 + x * 50
                alien_instance.y = 60 + y * 70
                self.aliens.append(alien_instance)

    def on_end(self):
        print("GameScene: on_end called")
        self.score = 0
        self.fighter = None
        self.aliens.clear()
        self.bombs.clear()
        self.explosions.clear()
        self.beams.clear()

    def on_key_down(self, key):
        # 왼쪽 이동
        if key == pygame.K_LEFT:
            self.fighter.direction_x = -1
        # 오른쪽 이동
        elif key == pygame.K_RIGHT:
            self.fighter.direction_x = 1
        # 빔
        elif key == pygame.K_z:
            self.beam_event()

    # 빔 생성 이벤트
    def beam_event(self):
        if len(self.beams) < 3:
            new_beam = Beam(self.fighter.x + self.fighter.image.get_width() / 2, self.fighter.y)
            self.beams.append(new_beam)
            self.soundMixer.shoot_sound.play()

    # Key Up
    def on_key_up(self, key):
        if key == pygame.K_LEFT or key == pygame.K_RIGHT:
            self.fighter.direction_x = 0

    # Update
    def on_update(self, delta_seconds):
        # 이동
        self.fighter.update(delta_seconds)

        # 모든 외계인 업데이트
        for alien in self.aliens:
            alien.update(delta_seconds)

            # 외계인 bomb 투척
            bomb = alien.shoot()
            if bomb is not None:
                self.bombs.append(bomb)

            # 외계인 -> fighter 충돌 체크
            if alien.check_collision([self.fighter]) is not None:
                # 외계인 폭발
                self.explosions.append(Explosion(alien.rect))
                # fighter 폭발
                self.explosions.append(Explosion(self.fighter.rect))
                # 외계인 제거
                self.aliens.remove(alien)
                self.soundMixer.explosion_sound.play()

                print("Game Over")
                data = {
                    "score": self.score
                }
                SceneManager.instance.change(GAME_OVER_SCENE_NAME,data)
                break

        # bombs 투척
        for bomb in self.bombs:
            bomb.update(delta_seconds)
            # 화면 밖으로 나가면 제거
            if SCREEN_HEIGHT < bomb.y:
                self.bombs.remove(bomb)
            else:
                if bomb.check_collision([self.fighter]) is not None:
                    self.explosions.append(Explosion(self.fighter.rect))
                    self.bombs.remove(bomb)
                    self.soundMixer.explosion_sound.play()
                    print("Game Over")
                    data = {
                        "score": self.score
                    }
                    SceneManager.instance.change(GAME_OVER_SCENE_NAME,data)
                    break

        # explosions 업데이트
        for explosion in self.explosions:
            explosion.update(delta_seconds)
            if explosion.is_finished():
                self.explosions.remove(explosion)

        # beam 이 존재하면 업데이트
        for beam in self.beams:
            beam.update(delta_seconds)
            if beam.y < 0:
                # 화면 밖으로 나가면 beam 제거
                self.beams.remove(beam)
            else:
                dead_alien = beam.check_collision(self.aliens)
                if dead_alien is not None:
                    self.explosions.append(Explosion(dead_alien.rect))
                    self.aliens.remove(dead_alien)
                    self.beams.remove(beam)
                    self.soundMixer.invaderKilled_sound.play()
                    self.add_score(10)
                    print("Score:", self.score)

                    if len(self.aliens) <= 0:
                        print("You Win!")
                        data = {
                            "score": self.score
                        }
                        SceneManager.instance.change(GAME_CLEAR_SCENE_NAME,data)
                    break

        # 방향 전환이 필요한 경우
        if Alien.should_change_direction:
            Alien.should_change_direction = False

            for alien in self.aliens:
                # 반대로
                alien.direction_x *= -1
                # 아래로 약간 이동
                alien.move(0, 50)

    # score 얻기
    def add_score(self, point):
        self.score += point

    # Rendering
    def on_render(self, surface):

        self.fighter.draw(surface)

        # beam 이 존재하면 그리기
        for beam in self.beams:
            beam.draw(surface)

        # 모든 외계인 그리기
        for alien in self.aliens:
            alien.draw(surface)

        # 모든 bombs 그리기
        for bomb in self.bombs:
            bomb.draw(surface)

        # 모든 explosions 그리기
        for explosion in self.explosions:
            explosion.draw(surface)

    def on_end_event(self):
        print("GameScene: on_end_event called")