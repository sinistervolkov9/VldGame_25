import sys
import timeit
import pygame as pg
from object_position_slot import ObjectPositionSlot
from screen import Screen
from settings import FPS, RES, SCREEN_POS
from markup import Markup
from scene_structure import SceneContent


class Scene:

    # --------------------------------------------- Инициализация ------------------------------------------------------

    def __init__(self, game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        # self.screen = pg.display.set_mode(RES, pg.FULLSCREEN)
        self.clock = pg.time.Clock()

        self.markup = None
        self.object_position_slot = None

        self.scene_sections = []
        self.scene_windows = []
        self.scene_content = SceneContent(
            self,
            self.scene_sections,
            self.scene_windows
        )

        self.current_section = None
        self.current_tab = None
        self.current_windows = []

        self.current_tab_index = None

        # ---

        self.visible_content = []
        self.active_content = []
        self.invisible_content = []
        self.inactive_content = []

        self.scene_screens = []
        self.scene_buttons_and_actions = []
        self.scene_buttons = []
        self.scene_sounds = []

        # ---

        self.header_screens = []
        self.header_buttons = []
        self.tab_screens = []
        self.tab_buttons = []
        self.background_screens = []
        self.background_buttons = []
        self.header_content = [self.header_screens, self.header_buttons]
        self.tab_content = None
        self.background_content = [self.background_screens, self.background_buttons]
        self.section_content = None
        self.visible_content_unpacked = [self.section_content]

        # ---

        # self.method_execution_time(self.declare_content)
        self.declare_content()
        self.validate_and_confirm_current_section_and_tab(self.current_section, self.current_tab)
        self.current_tab_index = self.get_current_tab_index(self.current_section)
        self.extract_scene_content(self.scene_content)
        self.build_visible_content_elements()
        self.update_visible_content()
        self.update_active_content()

        self.print_scene_state()
        self.print_visible_content_structure()

    def declare_content(self) -> None:
        """
        Инициализирует (объявляет) контент сцены.
        """
        self.markup = Markup(self)
        # self.screen_object_position_slot = Screen(self, None, (100, 100), None)
        # self.object_position_slot = ObjectPositionSlot(self, SCREEN_POS['c'], width=50, height=50, object=self.screen_object_position_slot)
        # self.object_position_slot = ObjectPositionSlot(self, SCREEN_POS['c'])

        # ! start declare scene content !
        # - objects -
        # ...

        # - Sections -
        # ...
        # - Windows -
        # ...

        # ! end declare scene content !

        self.scene_sections = []
        self.scene_windows = []

        self.scene_content = SceneContent(
            self,
            self.scene_sections,
            self.scene_windows
        )

        self.current_section = None
        self.current_tab = None
        self.current_windows = []

    # ------------------------------------------------ Управление ------------------------------------------------------

    def validate_and_confirm_current_section_and_tab(self, section, tab) -> None:
        """
        Проверяет корректность переданных параметров section и tab, а затем устанавливает их как текущие для сцены.

        :param section: Секция, которую нужно установить как текущую.
        :type section: Section
        :param tab: Вкладка, которую нужно установить как текущую.
        :type tab: Tab
        :raises ValueError: Если section или tab не указаны (None) или не найдены в соответствующих списках.
        """
        if section is None or tab is None:
            raise ValueError("Both section and tab must be specified (not None).")

        if section not in self.scene_sections:
            raise ValueError(f"Section '{section.name}' is not in the scene sections.")

        if tab not in section.get_tabs():
            raise ValueError(f"Tab '{tab.name}' is not in the section '{section.name}'.")

        self.current_section = section
        self.current_tab = tab
        print(f"Current section set to '{section.name}', current tab set to '{tab.name}'.")

    def extract_scene_content(self, scene_content) -> None:
        """
        Извлекает и обрабатывает содержимое сцены,
        собирая уникальные экраны, кнопки, звуки и др. объекты Сцены из секций (headers, tabs, backgrounds).

        :param scene_content: Объект, содержащий данные сцены.
        :type scene_content: SceneContent
        """
        screens_set = set()
        buttons_set = set()
        sounds_set = set()
        buttons_and_actions_list = []

        for section in scene_content.get_sections():
            for header in section.get_header():
                screens_set.update(header.get_screens())
                buttons_and_actions_list.extend(header.get_buttons())
            for tab in section.get_tabs():
                screens_set.update(tab.get_screens())
                buttons_and_actions_list.extend(tab.get_buttons())
                # sounds_set.update(tab.get_sounds())
            for background in section.get_background():
                screens_set.update(background.get_screens())
                buttons_and_actions_list.extend(background.get_buttons())

        for window in scene_content.get_windows():
            for header in window.get_header():
                screens_set.update(header.get_screens())
                buttons_and_actions_list.extend(header.get_buttons())
            for tab_window in window.get_tabs():
                screens_set.update(tab_window.get_screens())
                buttons_and_actions_list.extend(tab_window.get_buttons())
            for background in window.get_background():
                screens_set.update(background.get_screens())
                buttons_and_actions_list.extend(background.get_buttons())

        # Удаление дубликатов кнопок и действий
        unique_buttons = []
        for button in buttons_and_actions_list:
            if button not in unique_buttons:
                unique_buttons.append(button)

        self.scene_buttons_and_actions = unique_buttons

        # Отделение кнопок от их действий
        for button in self.scene_buttons_and_actions:
            for button_name, _ in button.items():
                buttons_set.add(button_name)

        self.scene_screens = list(screens_set)
        self.scene_sounds = list(sounds_set)
        self.scene_buttons = list(buttons_set)

    def build_visible_content_elements(self) -> None:
        """
        Собирает и обрабатывает видимые элементы контента текущей сцены.
        Этот метод приводит текущий контент к нужной форме для visible_content.
        """
        headers = self.current_section.get_header()
        tabs = self.current_section.get_tabs()
        backgrounds = self.current_section.get_background()

        self.header_screens = headers[0].get_screens()
        self.header_buttons = self.extract_buttons(headers[0].get_buttons())
        self.tab_screens = tabs[self.current_tab_index].get_screens()
        self.tab_buttons = self.extract_buttons(tabs[self.current_tab_index].get_buttons())
        self.background_screens = backgrounds[0].get_screens()
        self.background_buttons = self.extract_buttons(backgrounds[0].get_buttons())

        # Без проверок:
        # self.current_header_screens_unpacked = self.current_section.get_header()[0].get_screens()
        # self.current_header_buttons_unpacked = self.extract_buttons(self.current_section.get_header()[0].get_buttons())
        # self.current_tab_screens_unpacked = self.current_section.get_tabs()[self.current_tab_index].get_screens()
        # self.current_tab_buttons_unpacked = self.extract_buttons(
        #             self.current_section.get_tabs()[self.current_tab_index].get_buttons())
        # self.current_background_screens_unpacked = self.current_section.get_background()[0].get_screens()
        # self.current_background_buttons_unpacked = self.extract_buttons(
        #             self.current_section.get_background()[0].get_buttons())

        # С проверками:
        # self.current_header_screens_unpacked = [screen for screen in self.scene_screens if
        #                                         screen in self.current_section.get_header()[0].get_screens()]
        # self.current_header_buttons_unpacked = self.extract_buttons(
        #     [button for button in self.scene_buttons_and_actions if
        #      button in self.current_section.get_header()[
        #          0].get_buttons()])
        # self.current_tab_screens_unpacked = [screen for screen in self.scene_screens if
        #                                      screen in self.current_section.get_tabs()[
        #                                          self.current_tab_index].get_screens()]
        # self.current_tab_buttons_unpacked = self.extract_buttons([button for button in self.scene_buttons_and_actions if
        #                                                           button in self.current_section.get_tabs()[
        #                                                               self.current_tab_index].get_buttons()])
        # self.current_background_screens_unpacked = [screen for screen in self.scene_screens if
        #                                             screen in self.current_section.get_background()[0].get_screens()]
        # self.current_background_buttons_unpacked = self.extract_buttons(
        #     [button for button in self.scene_buttons_and_actions if
        #      button in self.current_section.get_background()[
        #          0].get_buttons()])

    def update_visible_content(self):
        """
        Обновляет видимый контент сцены, собирая данные из заголовка, текущей вкладки и фона текущего раздела в единый список.
        """
        self.header_content = [self.header_screens, self.header_buttons]
        self.tab_content = [self.tab_screens, self.tab_buttons]
        self.background_content = [self.background_screens, self.background_buttons]

        self.section_content = [self.background_content, self.tab_content, self.header_content]

        self.visible_content = [self.section_content]

    def update_active_content(self) -> None:
        """
        Обновляет активный контент сцены, добавляя все элементы из видимого контента в список активного контента.
        """
        for content_group in self.visible_content:
            for layer in content_group:
                if layer:
                    self.active_content.extend(layer)

    def extract_buttons(self, buttons_with_actions: list[dict[str, any]]) -> list[str]:
        """
        Извлекает объекты-кнопки (ключи из словарей) из списка кнопок с действиями и возвращает их в виде списка.

        :param buttons_with_actions: Список словарей, где ключи - имена кнопок, а значения - действия.
        :type buttons_with_actions: List[Dict[str, Any]]
        :return: Список объектов-кнопок
        :rtype: List[str]
        """
        buttons = []
        for button in buttons_with_actions:
            for button_name in button.keys():
                buttons.append(button_name)
        return buttons

    def get_current_tab_index(self, section) -> int:
        """
        Находит индекс текущей вкладки в указанном разделе.

        :param section: Раздел, в котором нужно найти индекс текущей вкладки.
        :type section: Section
        :return: Индекс текущей вкладки в разделе.
        :rtype: int
        :raises ValueError: Если текущая вкладка не найдена в разделе.
        """
        for index, tab in enumerate(section.get_tabs()):
            if tab == self.current_tab:
                return index
        raise ValueError(f"Current tab '{self.current_tab.name}' not found in section '{section.name}'.")

    def get_tab_by_name(self, section, name: str):
        """
        Ищет вкладку по имени в указанном разделе и возвращает её, если она найдена.
        Если вкладка не найдена, возвращает None.

        :param section: Раздел, в котором нужно найти вкладку.
        :type section: Section
        :param name: Имя вкладки, которую нужно найти.
        :type name: str
        :return: Найденная вкладка или None, если вкладка не найдена.
        :rtype: Optional[Tab]
        """
        for tab in section.get_tabs():
            if tab.name == name:
                return tab
        return None

    # --------------------------------------------- Обработка событий --------------------------------------------------

    def content_handle_event(self, event: any) -> None:
        """
        Обрабатывает событие, передавая его всем объектам видимого контента сцены.
        Использует рекурсивную функцию для обработки вложенных слоев контента.

        :param event: Событие, которое нужно обработать.
        :type event: Any
        """

        def handle_layer(layer):
            """
            Рекурсивно обрабатывает слой контента, передавая событие всем объектам в слое.

            :param layer: Слой контента, который нужно обработать.
            :type layer: Any
            """
            for content_object in layer:
                if isinstance(content_object, list):
                    handle_layer(content_object)
                else:
                    content_object.handle_event(event)

        for layer in self.visible_content:
            handle_layer(layer)

        # self.object_position_slot.handle_event(event)

    def check_userevent(self, event) -> None:
        """
        Проверяет пользовательское событие и, если оно соответствует определенным критериям,
        выполняет связанные с кнопкой действия.

        :param event: Событие, которое нужно проверить.
        :type event: Event
        """
        if event.type != pg.USEREVENT or not hasattr(event, 'button'):
            return

        for buttons_dict in self.scene_buttons_and_actions:
            button_name = list(buttons_dict.keys())[0]
            actions_list = list(buttons_dict.values())[0]

            if event.button == button_name:
                for action in actions_list:
                    for action_name, action_object in action.items():
                        self.execute_userevent(action_name, action_object)
                break
        else:
            print(f"event.button {event.button} not found in scene_buttons_and_actions")

    def execute_userevent(self, action_name: str, action_object: any) -> None:
        """
        Применяет пользовательское событие, выполняя соответствующее действие в зависимости от имени действия.

        :param action_name: Имя действия, которое нужно выполнить.
        :type action_name: str
        :param action_object: Объект, связанный с действием.
        :type action_object: Any
        """
        actions = {
            'print_event': self.print_event,
            'switch_scene': self.game.switch_scene,
            'switch_visibility': self.switch_visibility,
            'make_visible': self.make_visible,
            'make_invisible': self.make_invisible,
            'switch_activity': self.switch_activity,
            'play_sound': self.play_sound,
            'switch_tab': self.switch_tab,
        }

        if action_name in actions:
            print(f'\nExecute action: \n{action_name}')
            actions[action_name](action_object)
            # self.print_scene_state()
        else:
            print(f'\nUnknown action: \n{action_name}')

    def check_window_close(self, event):
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     if not self.screen_window.image_rect.collidepoint(event.pos):
        #         self.visible_content.remove(self.screen_window)
        pass

    # -------------------------------------------------- Действия ------------------------------------------------------

    def print_event(self, action_object):
        print(str(action_object))

    def switch_tab(self, action_object, activity_too=True):
        new_tab = self.get_tab_by_name(self.current_section, action_object)
        if new_tab:
            self.current_tab = new_tab
            self.current_tab_index = self.get_current_tab_index(self.current_section)
            self.build_visible_content_elements()
            self.update_visible_content()
        else:
            print('Вкладка не найдена')

        # self.current_tab = action_object
        # self.current_tab_index = self.get_current_tab_index(self.current_section)
        # self.build_visible_content_elements()
        # self.update_visible_content()

    def switch_visibility(self, action_object, activity_too=True):
        print(f'action_object - {action_object}')
        for obj in action_object:
            if obj in self.visible_content:
                self.visible_content.remove(obj)
                print(f'visible_content.remove({obj})')
                if activity_too is True:
                    if obj in self.active_content:
                        self.active_content.remove(obj)
                        print(f'active_content.remove({obj})')
                        self.inactive_content.append(obj)
                        print(f'inactive_content.append({obj})')
                if obj not in self.invisible_content:
                    self.invisible_content.append(obj)
                    print(f'invisible_content.append({obj})')
            elif obj in self.invisible_content:
                self.invisible_content.remove(obj)
                print(f'invisible_content.remove({obj})')
                if activity_too is True:
                    if obj not in self.active_content:
                        self.inactive_content.remove(obj)
                        print(f'inactive_content.remove({obj})')
                        self.active_content.append(obj)
                        print(f'active_content.append({obj})')
                if obj not in self.visible_content:
                    self.visible_content.append(obj)
                    print(f'visible_content.append({obj})')

        self.print_scene_state()

    def make_visible(self, action_object, activity_too=True):
        print(f'action_object - {action_object}')
        for obj in action_object:
            print(obj)
            if obj in self.invisible_content:
                self.invisible_content.remove(obj)
                print(f'invisible_content.remove({obj})')
                if activity_too is True:
                    if obj not in self.active_content:
                        self.inactive_content.remove(obj)
                        print(f'inactive_content.remove({obj})')
                        self.active_content.append(obj)
                        print(f'active_content.append({obj})')
                if obj not in self.visible_content:
                    self.visible_content.append(obj)
                    print(f'visible_content.append({obj})')

        self.print_scene_state()

    def make_invisible(self, action_object, activity_too=True):
        print(f'action_object - {action_object}')
        for obj in action_object:
            if obj in self.visible_content:
                self.visible_content.remove(obj)
                print(f'visible_content.remove({obj})')
                if activity_too is True:
                    if obj in self.active_content:
                        self.active_content.remove(obj)
                        print(f'active_content.remove({obj})')
                        self.inactive_content.append(obj)
                        print(f'inactive_content.append({obj})')
                if obj not in self.invisible_content:
                    self.invisible_content.append(obj)
                    print(f'invisible_content.append({obj})')

        self.print_scene_state()

    def switch_activity(self, action_object):
        print(f'action_object - {action_object}')
        for obj in action_object:
            if obj in self.active_content:
                self.active_content.remove(obj)
                print(f'active_content.remove({obj})')
                if obj not in self.inactive_content:
                    self.inactive_content.append(obj)
                    print(f'inactive_content.append({obj})')
            elif obj in self.inactive_content:
                self.inactive_content.remove(obj)
                print(f'inactive_content.remove({obj})')
                if obj not in self.active_content:
                    self.active_content.append(obj)
                    print(f'active_content.append({obj})')

        self.print_scene_state()

    def make_active(self, action_object):
        print(f'action_object - {action_object}')
        for obj in action_object:
            if obj in self.inactive_content:
                self.inactive_content.remove(obj)
                print(f'inactive_content.remove({obj})')
            if obj not in self.active_content:
                self.active_content.append(obj)
                print(f'active_content.append({obj})')

        self.print_scene_state()

    def make_inactive(self, action_object):
        print(f'action_object - {action_object}')
        for obj in action_object:
            if obj in self.active_content:
                self.active_content.remove(obj)
                print(f'active_content.remove({obj})')
            if obj not in self.inactive_content:
                self.inactive_content.append(obj)
                print(f'inactive_content.append({obj})')

        self.print_scene_state()

    # def change_screen_to(self, action_object, activity_too=True):  # Зачем?
    #     # print(f'current_screen - {self.current_screen}')
    #     if self.current_screen != action_object:
    #         if self.current_screen in self.visible_content:
    #             self.visible_content.remove(self.current_screen)
    #             # print(f'self.visible_content.remove({self.current_screen})')
    #             self.invisible_content.append(self.current_screen)
    #             # print(f'self.invisible_content.append({self.current_screen})')
    #             if activity_too is True:
    #                 if self.current_screen in self.active_content:
    #                     self.active_content.remove(self.current_screen)
    #                     # print(f'self.active_content.remove({self.current_screen})')
    #
    #         self.visible_content.insert(0, action_object)  # !
    #         self.current_screen = action_object
    #         if activity_too is True:
    #             if self.current_screen not in self.active_content:
    #                 self.active_content.append(self.current_screen)
    #                 # print(f'self.active_content.append({self.current_screen})')
    #
    #         # print(f'NEW current_screen - {self.current_screen}')

    # def open_window(self, action_object, activity_too=True):
    #     # Копирование и сохранение текущего состояния контента
    #     current_visible = self.visible_content.copy()
    #     current_invisible = self.invisible_content.copy()
    #     current_active = self.active_content.copy()
    #     current_inactive = self.inactive_content.copy()
    #
    #     self.make_visible(action_object, activity_too)  # отобразить окно и его контент
    #     self.make_inactive(current_active)  # добавить в неактивное всё, что было активно до открытия окна
    #
    #     self.print_scene_state()

    # def close_window(self, action_object, activity_too=True):
    #     # Вернуться к предыдущему состоянию контента из стэков
    #
    #     if not self.visible_stack or not self.active_stack or not self.invisible_stack or not self.inactive_stack:
    #         print("Нет окон для закрытия!")
    #         return
    #
    #     # self.make_invisible(action_object, activity_too)
    #     # self.make_active(self.active_content)  # активировать все то, что было активно до этого окна
    #
    #     self.print_scene_state()

    def play_sound(self, action_object):
        action_object.play_soundtrack()

    def esc_event(self):
        pass

    # --------------------------------------- Управление музыкой и обработка -------------------------------------------

    def play_soundtrack(self) -> None:
        """
        Проверяет, есть ли саундтрек для сцены и не играет ли он уже.
        Если саундтрек есть и не играет, загружает и запускает его.
        """
        if self.scene_soundtrack and not self.soundtrack_playing:
            pg.mixer.music.load(self.scene_soundtrack)
            pg.mixer.music.play(-1)
            self.soundtrack_playing = True

    def stop_soundtrack(self) -> None:
        """
        Останавливает воспроизведение саундтрека
        и обновляет соответствующий флаг.
        """
        pg.mixer.music.stop()
        self.soundtrack_playing = False

    def check_soundtrack_playing(self) -> None:
        """
        Проверяет, играет ли саундтрек в данный момент,
        и обновляет соответствующий флаг.
        """
        if not pg.mixer.music.get_busy():
            self.soundtrack_playing = False

    # -------------------------------------------------- Отладка -------------------------------------------------------

    def print_scene_state(self) -> None:
        """
        Обновляет страницу сцены, выводя на печать различные атрибуты и состояния сцены для отладки и проверки.
        """
        print(f'\nALL scene_screens - {self.scene_screens}')
        print(f'ALL scene_sounds - {self.scene_sounds}')
        print(f'ALL scene_buttons - {self.scene_buttons}')
        print(f'ALL scene_buttons_and_actions - {self.scene_buttons_and_actions}')

        print(f'\n!!! current_section - {self.current_section}')
        print(f'current_section_header - {self.current_section.get_header()}')
        print(f'current_section_tabs - {self.current_section.get_tabs()}')
        print(f'current_section_background - {self.current_section.get_background()}')

        print(f'\ncurrent_header - {self.current_section.get_header()}')
        print(f'!!! current_tab - {[self.current_tab]}')
        print(f'current_background - {self.current_section.get_background()}')

        print(f'\ncurrent_header_screen - {[header.get_screens() for header in self.current_section.get_header()]}')
        print(f'current_header_buttons - {[header.get_buttons() for header in self.current_section.get_header()]}')
        print(f'current_tab_screen - {[self.current_tab.get_screens()]}')
        print(f'current_tab_buttons - {[self.current_tab.get_buttons()]}')
        print(
            f'current_background_screen - {[background.get_screens() for background in self.current_section.get_background()]}')
        print(
            f'current_background_buttons - {[background.get_buttons() for background in self.current_section.get_background()]}')

        print(f"\nUpdated visible_content: {self.visible_content}")
        print(f"Updated active_content: {self.active_content}")

    def print_visible_content_structure(self) -> None:
        """
        Выводит структуру видимого контента сцены в виде дерева, используя рекурсивную функцию для обработки и вывода слоев с отступами.
        """

        def visualize_layer(layer, indent=0):
            """
            Рекурсивно обрабатывает и выводит слой с отступами.

            :param layer: Слой контента, который нужно визуализировать.
            :type layer: Any
            :param indent: Уровень вложенности для отступов.
            :type indent: int
            """
            prefix = "  " * indent  # Отступы
            if isinstance(layer, list):
                print(f"{prefix}[")
                for sublayer in layer:
                    visualize_layer(sublayer, indent + 1)
                print(f"{prefix}]")
            else:
                if hasattr(layer, '__class__'):
                    print(f"{prefix}{layer.__class__.__name__} - {layer}")
                else:
                    print(f"{prefix}{layer}")

        print("\nvisible_content structure:")
        visualize_layer(self.visible_content)

    def method_execution_time(self, method, *args, **kwargs) -> any:
        """
        Измеряет время выполнения переданного метода и выводит его.

        :param method: Метод, время выполнения которого нужно измерить.
        :type method: Callable
        :param args: Позиционные аргументы для передачи в метод.
        :param kwargs: Именованные аргументы для передачи в метод.
        :return: Результат выполнения метода.
        :rtype: Any
        """
        start_time = timeit.default_timer()
        result = method(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        print(f"Time taken to execute {method.__name__}: {execution_time} seconds")
        return result

    # ------------------------------------------------ Основной цикл ---------------------------------------------------

    def check_events(self) -> None:
        """
        Обрабатывает события, такие как закрытие окна или нажатие клавиши ESC,
        а также передает события другим методам для дальнейшей обработки.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            self.content_handle_event(event)
            self.check_userevent(event)
            # self.check_window_close(event)

    def update(self) -> None:
        """
        Обновляет состояние сцены, обновляя экран, поддерживая заданную частоту кадров
        и проверяя наведение курсора на объекты в видимом контенте.
        """
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption("Vld Game")

        def check_hover_layer(layer):
            """
            Рекурсивно проверяет наведение курсора на объекты в слое.

            :param layer: Слой контента, в котором нужно проверить наведение курсора.
            :type layer: Any
            """
            for obj in layer:
                if isinstance(obj, list):
                    check_hover_layer(obj)
                else:
                    obj.check_hover(pg.mouse.get_pos())

        for layer in self.visible_content:
            check_hover_layer(layer)

    def draw(self) -> None:
        """
        Рисует сцену, заполняя экран цветом, и рекурсивно рисуя все объекты в видимом контенте.
        """
        self.screen.fill("black")
        self.markup.draw()

        def draw_layer(layer):
            """
            Рекурсивно рисует все объекты в слое.

            :param layer: Слой контента, который нужно нарисовать.
            :type layer: Any
            """
            for obj in layer:
                if isinstance(obj, list):
                    draw_layer(obj)
                else:
                    obj.draw()

        # Итерируем по группам контента (раздел + окна)
        for content_group in self.visible_content:
            # Итерируем по слоям внутри группы (background, tabs, header)
            for layer in content_group:
                if not layer:  # Если слой пуст, пропускаем
                    continue
                draw_layer(layer)

        # for obj in self.visible_content:
        #     obj.draw()

        #  self.object_position_slot.draw()

    def run(self) -> None:
        """
        Запускает основной цикл сцены.
        """
        self.check_soundtrack_playing()
        # self.play_soundtrack()
        self.check_events()
        self.update()
        # self.update_visible_content()
        self.draw()
