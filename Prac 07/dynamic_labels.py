from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgets2(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strings = ["Brad", "Honey", "Beaver", "Hans", "Greta"]

    def build(self):
        self.title = "Dynamic Widgets 2"
        self.root = Builder.load_file('dynamic_widgets2.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for string in self.strings:
            temp_label = Label(text=string)
            self.root.ids.label_box.add_widget(temp_label)

DynamicWidgets2().run()