
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform
import requests

# Android permissions mangne ke liye
def request_android_permissions():
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.INTERNET])

class PlantApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Plant Identifier Ready\nClick button to Start", halign="center")
        self.add_widget(self.label)
        
        self.btn = Button(text="Identify Plant", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.call_api)
        self.add_widget(self.btn)

    def call_api(self, instance):
        self.label.text = "Connecting to Plant.id API..."
        # Yahan aapka API Key logic aayega

class MainApp(App):
    def build(self):
        if platform == 'android':
            request_android_permissions()
        return PlantApp()

if __name__ == "__main__":
    MainApp().run()
