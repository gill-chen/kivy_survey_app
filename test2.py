from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Declare both screens
class SurveyScreen(Screen):

    text = StringProperty("")
    # def change_text(self):
    #     self.text = "setting text works"

    def insert_data(self, age):
        self.text = age.text



class ResultScreen(Screen):
    age_text = StringProperty("")

class ConfirmationScreen(Screen):
    pass

class TestApp(App):
    pass

if __name__ == '__main__':
    TestApp().run()