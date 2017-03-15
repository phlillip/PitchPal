#!/usr/bin/env python3

import datetime

from kivy.app import App
from kivy.lang import Builder
Builder.load_file('PitchPal2.kv')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from time import strftime
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from functools import partial


class PitchPalApp(App):

    def build(self):
        return Builder.load_file('PitchPal2.kv')

    #   TEAM ADMIN FUNCTIONALITY

    #def on_enter(instance, value):
     #   print('User pressed enter in', instance)
      #  teamName = TextInput(text='Enter your team name', multiline=False)
     #   teamName.bind(on_text_validate=on_enter)

    #def on_text(instance, value):
     #   print('The widget', instance, 'have:', value)

    #teamName = TextInput()
    #teamName.bind(text=on_text)



    # STOPWATCH

    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            '%02d:%02d.%02d' %
            (int(minutes), int(seconds), int(seconds * 100 % 100)))

    # Stopwatch button
    def start_stop(self):

        global currentTime

        currentTime= self.root.ids.stopwatch.text[:-6]

        if self.root.ids.start_stop.text == "Start":
            self.sw_started = True
            print(currentTime + ' Kick off.')
            self.root.ids.start_stop.text = "End half"
        elif self.root.ids.start_stop.text == "End half":
            self.sw_started = False
            self.sw_seconds = 2700
            self.root.ids.start_stop.text = "Start second half"
        elif self.root.ids.start_stop.text == "Start second half":
            self.sw_started = True
            self.root.ids.start_stop.text = "End 90 minutes"
        elif self.root.ids.start_stop.text == "End 90 minutes":
            self.sw_started = False
            self.sw_seconds = 5400
            self.root.ids.start_stop.text = "Generate Match Report"

        return currentTime

    # Match event button
    def matchEvent(self):
        currentTime = self.root.ids.stopwatch.text[:-6]
        currentTime = int(currentTime) + 1


        # Select player and close player list
        def capture_player(name):
            event_player = name.text
            popup_player_list.dismiss()

            # Select event and publish
            def capture_event(name):
                event_name = name.text
                event_log = (str(currentTime).zfill(2) + ' ' + event_name + ' (' + event_player +')')
                print(event_log)
                self.root.ids.commentary.text += '\n' + event_log
                popup_event_list.dismiss()

            # Build event list modal
            layout_event_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
            layout_event_list.bind(minimum_height=layout_event_list.setter('height'))
            list_of_events = ["Goal scored", "Goal conceded", "Yellow card", "Red card"]
            layout_event_list.my_buttons = []  # if you want to keep an "easy" reference to your buttons to do something with them later
            # kivy doesnt crashes because it creates the property automatically
            for event in list_of_events:
                button = Button(text=event, size_hint_y=None, height=50)
                button.bind(on_press=capture_event)
                layout_event_list.my_buttons.append(button)
                layout_event_list.add_widget(button)

            root = ScrollView(size_hint=(1, None), size=(Window.width * 1, Window.height * .9))
            root.add_widget(layout_event_list)

            # Open event modal
            popup_event_list = Popup(title='Select event:', content=root, size_hint=(1, 1))
            popup_event_list.open()

        # Build player list modal
        layout_popup_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        layout_popup_list.bind(minimum_height=layout_popup_list.setter('height'))
        list_of_players = ["John D", "Ashley Holdstock", "Neil Seager", "Jordan Price",
                           "Mark Randle", "Stuart Tomlinson", "Kieran Price", "Max Barnes",
                           "Anthony Bromhead", "Matthew Wood", "Paul Jeynes", "Phillip Penny"]
        layout_popup_list.my_buttons = []  # if you want to keep an "easy" reference to your buttons to do something with them later
        # kivy doesnt crashes because it creates the property automatically
        for player in list_of_players:
            button = Button(text=player, size_hint_y=None, height=50)
            button.bind(on_press=capture_player)
            layout_popup_list.my_buttons.append(button)
            layout_popup_list.add_widget(button)

        root = ScrollView(size_hint=(1, None), size=(Window.width * 1, Window.height * .9))
        root.add_widget(layout_popup_list)

        # Open player list modal
        popup_player_list = Popup(title='Select player:', content=root, size_hint=(1, 1))
        popup_player_list.open()



if __name__ == '__main__':
    PitchPalApp().run()
