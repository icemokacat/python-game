
class BaseScene:
    def on_begin(self):
        pass

    def on_end(self):
        pass

    def on_key_down(self, key):
        pass

    def on_key_up(self, key):
        pass

    def on_update(self, delta_seconds):
        pass

    def on_render(self, surface):
        pass

    def on_end_event(self):
        pass

    def set_data(self, data):
        pass