#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Christian Antony Quero"
__version__ = "0.1.0"
__license__ = "MIT"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        print("Working")
        self.manager.current_screen.ids.img.source = 'files/images/down.png'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


class Webcam:
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class FileSharer:
    def __init__(self, filepath, api):
        self.filepath = filepath
        self.api = api

    def share(self):
        pass


def main():
    """ Main entry point of the app """
    MainApp().run()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
