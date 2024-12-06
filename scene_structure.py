class SceneContent:
    def __init__(self, game, sections: list, windows: list):
        self.game = game
        self.sections = sections
        self.windows = windows

    def get_sections(self):
        return self.sections

    def get_windows(self):
        return self.windows


class SectionOrWindow:
    def __init__(self, game, name: str, description: str, header: list, tabs: list, background: list):
        self.game = game
        self.name = name
        self.description = description
        self.header = header
        self.tabs = tabs
        self.background = background

    def get_header(self):
        return self.header

    def get_tabs(self):
        return self.tabs

    def get_background(self):
        return self.background


class Header:
    def __init__(self, game, name: str, description: str, screens: list, buttons: list):
        self.game = game
        self.name = name
        self.description = description
        self.screens = screens
        self.buttons = buttons

    def get_screens(self):
        return self.screens

    def get_buttons(self):
        return self.buttons


class Tab:
    def __init__(self, game, name: str, description: str, screens: list, buttons: list, sounds: list):
        self.game = game
        self.name = name
        self.description = description
        self.screens = screens
        self.buttons = buttons
        self.sounds = sounds

    def get_screens(self):
        return self.screens

    def get_buttons(self):
        return self.buttons

    def get_sounds(self):
        return self.sounds


class Background:
    def __init__(self, game, name: str, description: str, screens: list, buttons: list):
        self.game = game
        self.name = name
        self.description = description
        self.screens = screens
        self.buttons = buttons

    def get_screens(self):
        return self.screens

    def get_buttons(self):
        return self.buttons


# class TabWindow:
#     def __init__(self, game, name: str, description: str, screens: list, buttons: list):
#         self.game = game
#         self.name = name
#         self.description = description
#         self.screens = screens
#         self.buttons = buttons
#
#     def get_screens(self):
#         return self.screens
#
#     def get_buttons(self):
#         return self.buttons
