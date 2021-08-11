from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class CanvasExample1(Widget):
    pass


class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('No click yet')
    slider_value_txt = StringProperty('Slider disabled')
    text_input_str = StringProperty('foo')
    
    def on_toggle_button_state(self, widget):
        print(f'toggel state: {widget.state}')
        if widget.state == 'normal':
            widget.text = 'OFF'
            self.count_enabled = False
        elif widget.state == 'down':
            widget.text = 'ON'
            self.count_enabled = True
            

    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = f'Clicks: {self.count}'

    def on_switch_active(self, widget):
        if not widget.active:
            self.slider_value_txt = 'Slider disabled'
        print(f'Switch: {widget.active}')

    def on_slider_value(self, widget):
        self.slider_value_txt = str(int(widget.value))
        # print(f'Slider: {int(widget.value)}')
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text



class StackLayoutExample(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 100):
            b = Button(text=str(i), size_hint=(.2, .2))
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass
 

if __name__ == '__main__':
    TheLabApp().run()