import pygame as pg
from settings import BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_SCALE, SCREEN_POS


class Button:
    def __init__(self,
                 game,
                 text='text',
                 pos=None,
                 image_basic=None, image_hover=None, image_press=None,
                 sound_hover=True, sound_click=True
                 ):
        self.game = game

        self.text = 'button' if text is None else " ".join(text.split())

        # self.pos = SCREEN_POS["tl"] if pos is None else pos

        self.image = 'resources/button/default/button.png' if image_basic is None else image_basic
        self.image_hover = 'resources/button/default/button_hovered.png' if image_hover is None else image_hover
        self.image_press = 'resources/button/default/button_pressed.png' if image_press is None else image_press

        # self.sound_hover = 'resources/sounds/default_sound_hover.wav' if sound_hover is None else sound_hover
        # self.sound_click = 'resources/sounds/default_sound_click.wav' if sound_click is None else sound_click

        if sound_hover is True:
            self.sound_hover = 'resources/sounds/default_sound_hover.wav'
        elif sound_hover is False or sound_hover is None:
            self.sound_hover = None
        else:
            self.sound_hover = sound_hover

        if sound_click is True:
            self.sound_click = 'resources/sounds/default_sound_click.wav'
        elif sound_click is False or sound_click is None:
            self.sound_click = None
        else:
            self.sound_click = sound_click

        # ---

        self.scale = BUTTON_SCALE
        self.w = BUTTON_WIDTH  # Ширина
        self.h = BUTTON_HEIGHT  # Высота
        self.is_hovered = False
        self.is_press = False
        self.over = False

        if pos is None:
            self.pos = self.x, self.y = SCREEN_POS["tl"][0] - self.w * self.scale / 2, SCREEN_POS["tl"][1] - self.h * self.scale / 2
        else:
            self.pos = self.x, self.y = pos[0] - self.w * self.scale / 2, pos[1] - self.h * self.scale / 2

        # ---

        self.load_images()
        self.load_sounds()
        self.get_size_pos()
        self.update()  # ?

    def load_images(self):
        self.image = pg.image.load(self.image)
        self.image_hover = pg.image.load(self.image_hover)
        self.image_press = pg.image.load(self.image_press)

    def load_sounds(self):
        if self.sound_hover:
            self.sound_hover = pg.mixer.Sound(self.sound_hover)
        if self.sound_click:
            self.sound_click = pg.mixer.Sound(self.sound_click)

    def get_size_pos(self):
        self.size_button = (self.w * self.scale, self.h * self.scale)
        self.pos_button = self.pos

    def check_hover(self, mouse_pos):
        self.is_hovered = self.image_rect.collidepoint(mouse_pos)

    def update(self):
        self.image = pg.transform.scale(self.image, self.size_button)
        self.image_rect = self.image.get_rect(topleft=self.pos_button)

        self.image_hover = pg.transform.scale(self.image_hover, self.size_button)
        # self.image_hover_rect = self.image_hover.get_rect(topleft=self.pos_button)

        self.image_press = pg.transform.scale(self.image_press, self.size_button)
        # self.image_press_rect = self.image_press.get_rect(topleft=self.pos_button)

        # ---

        self.get_font_size_text()

        # ---

        text_font = pg.font.Font(None, self.font_size_text)
        self.text_text_surface = text_font.render(self.text, True, "white")
        self.text_text_rect = self.text_text_surface.get_rect(
            center=(self.image_rect.centerx, self.image_rect.centery))

    def get_font_size_text(self):
        number_of_reductions = 4  # 4

        start_number_of_symbols = 7  # 7
        add_symbols = 2  # 2

        symbols_scale = 0.5  # 0.5
        add_scale = 0.05  # 0.05

        if len(self.text) > int(start_number_of_symbols + number_of_reductions * add_symbols - add_symbols):
            self.text = self.text[
                        :int(start_number_of_symbols + number_of_reductions * add_symbols - add_symbols) - 3] + "..."
            end_symbols_scale = symbols_scale + add_scale * (number_of_reductions - 1)
            self.font_size_text = int(self.scale - self.scale * end_symbols_scale)
        else:
            for i in range(number_of_reductions):
                if len(self.text) <= start_number_of_symbols:
                    self.font_size_text = int(self.scale - self.scale * symbols_scale)
                    break
                else:
                    symbols_scale += add_scale
                    start_number_of_symbols += add_symbols

    def draw(self):
        pressed = pg.mouse.get_pressed()

        if self.is_press:
            current_image = self.image_press
        elif self.is_hovered and not pressed[0]:
            current_image = self.image_hover
        else:
            current_image = self.image

        self.game.screen.blit(current_image, self.image_rect.topleft)
        self.game.screen.blit(self.text_text_surface, self.text_text_rect)

    def handle_event(self, event):
        pressed = pg.mouse.get_pressed()

        if self.is_hovered:
            if not self.over:
                if self.sound_hover:
                    self.sound_hover.play()
                self.over = True
        else:
            self.over = False

        if pressed[0] and not self.is_hovered:
            self.is_hovered = False
            self.is_press = False
            self.over = True

        if self.is_hovered and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.is_press = True

        if self.is_hovered and self.is_press and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.sound_click:
                self.sound_click.play()
            self.is_press = False
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
