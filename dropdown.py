from kivymd.app import MDApp
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen


class MyScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define dropdown items
        items = [{"text": f"Item {i}"} for i in range(1, 6)]

        # Create dropdown menu
        self.dropdown_menu = MDDropdownMenu(
            caller=self.ids.dropdown_item,
            items=items,
            width_mult=4,
        )

    def on_dropdown_select(self, instance, value):
        # Do something with selected value
        print(f"Selected value: {value}")

class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MyScreen()
        return screen


if __name__ == '__main__':
    MyApp().run()
