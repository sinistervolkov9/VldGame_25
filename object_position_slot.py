import pygame as pg


class ObjectPositionSlot:
    def __init__(self, game, pos, width=50, height=50, object=None):
        self.game = game
        self.pos = list(pos)  # x, y координаты, изменяемые
        self.width = width
        self.height = height
        self.object = object if object is not None else None  # Хранит объект или None, если слот пуст
        self.is_dragging = False  # Флаг, активен ли перетаскиваемый слот

    def attach_object(self, obj):
        """Привязать объект к слоту"""
        self.object = obj

    def detach_object(self):
        """Отвязать объект от слота"""
        self.object = None

    def handle_event(self, event):
        """Обработка событий для drag and drop"""
        if event.type == pg.MOUSEBUTTONDOWN:
            print('event.type == pg.MOUSEBUTTONDOWN')
            # Проверяем, нажата ли мышка внутри слота
            mouse_x, mouse_y = event.pos
            if self.object:
                self.object.image = pg.transform.scale(self.object.image, self.object.size)
                self.object.image_rect = self.object.image.get_rect(topleft=self.pos)
                if self.object.image_rect.collidepoint(mouse_x, mouse_y):
                    print('rect.collidepoint')
                    self.is_dragging = True
            else:
                rect = pg.Rect(self.pos[0] - self.width // 2,
                               self.pos[1] - self.height // 2,
                               self.width,
                               self.height)
                if rect.collidepoint(mouse_x, mouse_y):
                    print('rect.collidepoint')
                    self.is_dragging = True

        elif event.type == pg.MOUSEBUTTONUP:
            print('event.type == pg.MOUSEBUTTONUP')
            # Отпускаем слот
            self.is_dragging = False

        elif event.type == pg.MOUSEMOTION:
            print('event.type == pg.MOUSEMOTION')
            # Перемещаем слот, если идет перетаскивание
            if self.is_dragging:
                print('self.is_dragging')
                self.pos[0] += event.rel[0]
                self.pos[1] += event.rel[1]

    def draw(self):
        """Отрисовка слота"""
        if self.object is None:
            # Рисуем зеленый квадрат, если слот пуст
            rect = pg.Rect(self.pos[0] - self.width // 2,
                           self.pos[1] - self.height // 2,
                           self.width,
                           self.height)
            pg.draw.rect(self.game.screen, "green", rect)
        else:
            # Отображаем объект, если он есть
            self.object.draw()

    def check_hover(self, mouse_pos):
        pass
