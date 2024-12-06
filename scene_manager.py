from settings import SCREEN_POS
from scene import Scene
from scene_structure import SceneContent, SectionOrWindow, Header, Tab, Background
from button import Button
from screen import Screen
from soundtrack import Soundtrack


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        # ! start declare scene content !
        # - objects -

        self.screen_header_sec1 = Screen(self, None, (600, 100), 'resources/backgrounds/background.jpg')
        self.button1_header_sec1 = Button(self, 'switch_scene', SCREEN_POS['tc1'])
        self.screen_tab1_sec1 = Screen(self, None, None, None)
        self.button1_tab1_sec1 = Button(self, 'switch_tab', SCREEN_POS['c'])
        self.screen_tab2_sec1 = Screen(self, None, None, 'resources/backgrounds/background_2.png')
        self.button1_tab2_sec1 = Button(self, 'switch_tab', SCREEN_POS['tc3'])
        self.screen_tab3_sec1 = Screen(self, None, None, 'resources/backgrounds/default_background.jpg')
        self.button1_tab3_sec1 = Button(self, 'switch_tab', SCREEN_POS['bc3'])
        self.button2_tab3_sec1 = Button(self, 'switch_scene', SCREEN_POS['bc1'])
        self.screen_background_sec1 = Screen(self, None, (600, 100), 'resources/backgrounds/background.jpg')
        self.button1_background_sec1 = Button(self, 'action', SCREEN_POS['br11'])

        self.sound_1 = Soundtrack(self, True)

        # - Sections -
        # -- Section_1 --
        # --- Section_1 header ---
        self.header_sec1 = Header(
            self,
            'header_sec1',
            'description',
            [
                self.screen_header_sec1,
            ],
            [
                {self.button1_header_sec1: [
                    {'switch_scene': 'scene_2'},
                ]},
            ]
        )

        # --- Section_1 tabs ---
        # ---- tab ----
        self.tab1_sec1 = Tab(
            self,
            'tab1_sec1',
            'description',
            [
                self.screen_tab1_sec1,
            ],
            [
                {self.button1_tab1_sec1: [
                    {'switch_tab': 'tab2_sec1'},
                ]},
            ],
            [
                self.sound_1
            ]
        )

        # ---- tab ----
        self.tab2_sec1 = Tab(
            self,
            'tab2_sec1',
            'description',
            [
                self.screen_tab2_sec1,
            ],
            [
                {self.button1_tab2_sec1: [
                    {'switch_tab': 'tab3_sec1'},
                    # {'switch_tab': 'tab1_sec1'},
                ]},
            ],
            [
                self.sound_1
            ]
        )

        # ---- tab ----
        self.tab3_sec1 = Tab(
            self,
            'tab3_sec1',
            'description',
            [
                self.screen_tab3_sec1,
            ],
            [
                {self.button1_tab3_sec1: [
                    {'switch_tab': 'tab1_sec1'},
                    # {'switch_tab': 'tab1_sec1'},
                ]},
                {self.button2_tab3_sec1: [
                    {'switch_scene': 'scene_2'},
                ]},
            ],
            [
                self.sound_1
            ]
        )

        # --- Section_1 background ---
        self.background_sec1 = Background(
            self,
            'background_1',
            'description',
            [
                self.screen_background_sec1,
            ],
            [
                {self.button1_background_sec1: [
                    {'action': 'action'},
                    {'play_sound': self.sound_1},
                ]},
            ]
        )

        # --- Section_1 build ---
        self.section_1 = SectionOrWindow(
            self,
            'section_1',
            'description',
            [
                self.header_sec1
            ],
            [
                self.tab1_sec1,
                self.tab2_sec1,
                self.tab3_sec1,
            ],
            [
                self.background_sec1,
            ]
        )

        # - Windows -
        # -- Window_1 --
        # --- Window_1 header ---

        # --- Window_1 tabs ---

        # --- Window_1 background ---

        # --- Window_1 build ---
        self.window_1 = SectionOrWindow(
            self,
            'window_1',
            'description',
            [

            ],
            [

            ],
            [

            ]
        )

        # ! end declare scene content !

        self.scene_sections = [
            self.section_1,
        ]
        self.scene_windows = [
            self.window_1,
        ]

        self.scene_content = SceneContent(
            self,
            self.scene_sections,
            self.scene_windows
        )

        self.current_section = self.scene_sections[0]
        self.current_tab = self.current_section.get_tabs()[0]

        # # Добавление большого количества объектов для тестирования производительности
        # for i in range(1000):
        #     screen = Screen(self, None, None, None)
        #     button = Button(self, f'button_{i}', SCREEN_POS['tl11'])
        #     tab = Tab(
        #         self,
        #         f'tab_{i}',
        #         'description',
        #         [
        #             screen,
        #         ],
        #         [
        #             {button: [
        #                 {'switch_scene': 'scene_2'},
        #             ]},
        #         ],
        #         [
        #             self.sound_1
        #         ]
        #     )
        #     self.section_1.tabs.append(tab)

# ----------------------------------------------------------------------------------------------------------------------

class SceneNext(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        # ! start declare scene content !
        # - objects -
        self.screen_tab1_sec1 = Screen(self, None, None, None)
        self.button1_tab1_sec1 = Button(self, 'switch_tab', SCREEN_POS['tl33'])
        self.screen_tab2_sec1 = Screen(self, None, None, 'resources/backgrounds/background_2.png')
        self.button1_tab2_sec1 = Button(self, 'switch_scene', SCREEN_POS['tr33'])

        # - Sections -
        # -- Section_1 --
        # --- Section_1 header ---
        self.header_sec1 = Header(
            self,
            'header_sec1',
            'description',
            [

            ],
            [

            ]
        )

        # --- Section_1 tabs ---
        # ---- tab ----
        self.tab1_sec1 = Tab(
            self,
            'tab1_sec1',
            'description',
            [
                self.screen_tab1_sec1,
            ],
            [
                {self.button1_tab1_sec1: [
                    {'switch_tab': 'tab2_sec1'},
                    {'print_event': 'Алло'},
                ]},
            ],
            [

            ]
        )

        # ---- tab ----
        self.tab2_sec1 = Tab(
            self,
            'tab2_sec1',
            'description',
            [
                self.screen_tab2_sec1,
            ],
            [
                {self.button1_tab2_sec1: [
                    {'switch_tab': 'tab1_sec1'},
                    {'switch_scene': 'scene_1'},
                ]},
            ],
            [

            ]
        )

        # --- Section_1 background ---
        self.background_sec1 = Background(
            self,
            'background_1',
            'description',
            [

            ],
            [

            ]
        )

        # --- Section_1 build ---
        self.section_1 = SectionOrWindow(
            self,
            'section_1',
            'description',
            [
                self.header_sec1
            ],
            [
                self.tab1_sec1,
                self.tab2_sec1,
            ],
            [
                self.background_sec1,
            ]
        )

        # - Windows -
        # -- Window_1 --
        # --- Window_1 header ---

        # --- Window_1 tabs ---

        # --- Window_1 background ---

        # --- Window_1 build ---
        self.window_1 = SectionOrWindow(
            self,
            'window_1',
            'description',
            [

            ],
            [

            ],
            [

            ]
        )

        # ! end declare scene content !

        self.scene_sections = [
            self.section_1,
        ]
        self.scene_windows = [
            self.window_1,
        ]

        self.scene_content = SceneContent(
            self,
            self.scene_sections,
            self.scene_windows
        )

        self.current_section = self.scene_sections[0]
        self.current_tab = self.current_section.get_tabs()[0]

# ----------------------------------------------------------------------------------------------------------------------
