from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETERS_CONSTANT = 1.60934

class Convert(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert.kv')
        return self.root

    def convert(self):
        m = int(self.root.ids.text_input.text)
        km = m * MILES_TO_KILOMETERS_CONSTANT
        self.root.ids.output_text.text= str(km)

    def up(self):
        self.root.ids.text_input.text = str(int(self.root.ids.text_input.text) + 1)

    def down(self):
        self.root.ids.text_input.text = str(int(self.root.ids.text_input.text) - 1)

Convert().run()