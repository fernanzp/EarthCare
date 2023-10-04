from pygame import mixer


class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.soundtrack = mixer.Sound("Resourses/sfx/main_theme.wav")
        self.forest_soundtrack = mixer.Sound("Resourses/sfx/forest_level_sound.wav")
        self.beach_soundtrack = mixer.Sound("")
        self.city_soundtrack = mixer.Sound("Resourses/sfx/city_level_sound.wav")
    def play_sfx(self, sfx):
        if self.allowSFX:
            self.sfx_channel.play(sfx)

    def play_music(self, music):
            self.music_channel.play(music)
