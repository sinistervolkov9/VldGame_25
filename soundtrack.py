import pygame as pg


class Soundtrack:
    def __init__(self,
                 game,
                 sound=True):
        self.game = game

        if sound is True:
            self.sound = 'resources/sounds/scroll_click_1.wav'
        elif sound is False or sound is None:
            self.sound_click = None
        else:
            self.sound = sound

        self.load_sounds()

    def load_sounds(self):
        # pg.mixer.music.load(self.sound)
        self.sound = pg.mixer.Sound(self.sound)

    def play_soundtrack(self):
        # pg.mixer.music.play
        self.sound.play()
