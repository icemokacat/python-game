import pygame
import utils.assetUtils as assetUtils

class MixerContainer:
    def __init__(self):
        self.shoot_sound            = pygame.mixer.Sound(assetUtils.get_asset_sound_path("shoot.wav"))
        self.explosion_sound        = pygame.mixer.Sound(assetUtils.get_asset_sound_path("explosion.wav"))
        self.invaderKilled_sound    = pygame.mixer.Sound(assetUtils.get_asset_sound_path("invaderkilled.wav"))
        self.ufo_highpitch_sound    = pygame.mixer.Sound(assetUtils.get_asset_sound_path("ufo_highpitch.wav"))
        self.ufo_lowpitch_sound     = pygame.mixer.Sound(assetUtils.get_asset_sound_path("ufo_lowpitch.wav"))

        self.shoot_sound.set_volume(0.1)
        self.explosion_sound.set_volume(0.1)
        self.invaderKilled_sound.set_volume(0.1)
        self.ufo_highpitch_sound.set_volume(0.1)
        self.ufo_lowpitch_sound.set_volume(0.1)

