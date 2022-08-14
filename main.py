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
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        print(f"Searching '{query}'")

        # Get wikipedia page
        page = wikipedia.page(query)
        images = page.images
        if len(images) > 0:
            image_link = images[0]

        # Download Image
        print(f"Downloading image {image_link}")
        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        req = requests.get(image_link, headers=headers)

        image_name = query + '.jpg'
        image_path = "files/images/" + image_name

        with open(image_path, 'wb') as file:
            file.write(req.content)

        file.close()
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = image_path


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
