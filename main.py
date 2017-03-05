from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Phone>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'home'
                Label:
                    markup: True
                    text: 'Home'
            Screen:
                name: 'squad'
                Label:
                    markup: True
                    text: 'Squad'
            Screen:
                name: 'matchday'
                Label:
                    markup: True
                    text: 'Matchday'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Home'
                on_press:
                    _screen_manager.current = 'home'
                    _screen_manager.transition.direction = 'right'
            Button:
                text: 'Squad'
                on_press:
                    if(_screen_manager.current == 'home'): _screen_manager.transition.direction = 'left'
                    else: _screen_manager.transition.direction = 'right'

                    _screen_manager.current = 'squad'

            Button:
                text: 'Matchday'
                on_press:
                    _screen_manager.current = 'matchday'
                    _screen_manager.transition.direction = 'left'""")


class Phone(FloatLayout):
    pass


class PitchPalApp(App):
    def build(self):
        return Phone()


if __name__ == '__main__':
    PitchPalApp().run()
