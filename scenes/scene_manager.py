
class SceneManager:
    instance = None

    def __init__(self):
        self.scenes = {}
        self.scene = None

    def add(self, name, scene):
        self.scenes[name] = scene
        if self.scene is None:
            self.scene = scene
            self.scene.on_begin()

    def change(self, name, prev_scene_data=None):
        self.scene.on_end()
        self.scene = self.scenes[name]
        self.scene.set_data(prev_scene_data)
        self.scene.on_begin()

SceneManager.instance = SceneManager()