from pygame import *

class Settings:
    def __init__(self):
        self.music_enabled = True
        self.music_volume = 0.5
        self.host = "localhost"
        self.port = 8081


# -- music functions --
def apply_volume(settings):
    mixer.music.set_volume(settings.music_volume)

def toggle_music(settings):
    settings.music_enabled = not settings.music_enabled
    if settings.music_enabled:
        mixer.music.set_volume(settings.music_volume)
        mixer.music.play(-1)
    else:
        mixer.music.stop()

def increase_volume(settings):
    settings.volume = max(0, min(1, settings.volume + 0.05))
    apply_volume(settings)

def decrease_volume(settings):
    settings.volume = max(0, min(1, settings.volume - 0.05))
    apply_volume(settings)

class SettingsItem:
    def __init__(self, label, type, rect, get_value, set_value = None,
                 set_value_up = None, set_value_down = None):
        self.label = label
        self.type = type
        self.rect = rect
        self.get_value = get_value
        self.set_value = set_value
        self.set_value_up = set_value_up
        self.set_value_down = set_value_down
        self.editing = False