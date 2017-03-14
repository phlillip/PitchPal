#!/usr/bin/env python3

import datetime

from kivy.app import App
from kivy.lang import Builder
Builder.load_file('PitchPal2.kv')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from time import strftime
from kivy.properties import ObjectProperty

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

    #CLOCK

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

    def start_stop(self):

        currentTime = self.root.ids.stopwatch.text[:-3]

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

    def matchEvent(self):
        print (self.start_stop() + ' GOAL for Redolence!!!')


if __name__ == '__main__':
    PitchPalApp().run()
