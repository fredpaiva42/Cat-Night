import pygame


class MusicManager:
    def __init__(self):
        self.sounds = {}
        self.loadSounds()

    def loadSounds(self):
        self.sounds["menu"] = "../sound/music/title.wav"
        self.sounds["background"] = "../sound/music/background.wav"
        self.sounds["boss_fight"] = "../sound/music/boss_fight.wav"
        self.sounds["win"] = "../sound/music/background.wav"
        self.sounds["defeat"] = "../sound/music/defeat.wav"

        self.sounds["item_collect"] = "../sound/sound-effects/item_collect.wav"
        self.sounds["enemyhit"] = "Sound/enemy_hit.wav"

    def loadSound(self, name, volume):
        soundEffect = pygame.mixer.Sound(self.sounds[name])
        soundEffect.set_volume(volume)
        soundEffect.play()

    def loadMusic(self, name, volume, num = -1):
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(self.sounds[name])
        pygame.mixer.music.play(num)

    def pause(self):
        pygame.mixer.music.pause()

    def play(self):
        pygame.mixer.music.unpause()
