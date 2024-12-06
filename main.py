from scene_manager import SceneMainMenu, SceneNext


class Game:
    def __init__(self):
        self.scene_1 = SceneMainMenu(self)
        self.scene_2 = SceneNext(self)

        # ---

        self.game_scenes = [
            {'scene_1': self.scene_1},
            {'scene_2': self.scene_2},
        ]

        # ---

        self.current_scene = self.scene_1

    def switch_scene(self, new_scene):
        for scene in self.game_scenes:
            for scene_name, scene_object in scene.items():
                if new_scene == scene_name:
                    self.current_scene.stop_soundtrack()
                    self.current_scene = scene_object

    def run_game(self):
        while True:
            self.current_scene.run()


if __name__ == "__main__":
    game = Game()
    # print(game.current_scene)
    game.run_game()
