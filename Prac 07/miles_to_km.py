from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934

class MilesToKilometre(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.validate_number()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_number.text = str(result)

    def change_value(self, change):
        new_value = self.validate_number() + change
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate()

    def validate_number(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0

MilesToKilometre().run()