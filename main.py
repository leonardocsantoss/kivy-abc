#!/usr/bin/env python

from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.gesture import Gesture, GestureDatabase

from gestures import gestures

import random


class GestureBoard(FloatLayout):
    ponts = 0

    def __init__(self, *args, **kwargs):
        super(GestureBoard, self).__init__()
        self.gdb = GestureDatabase()

        #Gestures
        for key, ges in gestures.items():
            self.gdb.add_gesture(ges)

        self.sort_letter()


    def sort_letter(self):
        self.letter = random.choice(gestures.keys())
        letter_button = Button(
            text=self.letter,
            size_hint=(.1, .1),
            pos_hint={'x':0, 'y':.9}
        )
        self.add_widget(letter_button)
        ponts_button = Button(
            text=u"Pontos: %s" % self.ponts,
            size_hint=(.3, .1),
            pos_hint={'x':.7, 'y':.9}
        )
        self.add_widget(ponts_button)


    def on_touch_down(self, touch):
        # start collecting points in touch.ud
        # create a line to display the points
        userdata = touch.ud
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            userdata['line'] = Line(points=(touch.x, touch.y))
        return True

    def on_touch_move(self, touch):
        # store points of the touch movement
        try:
            touch.ud['line'].points += [touch.x, touch.y]
            return True
        except (KeyError) as e: pass

    def on_touch_up(self, touch):
        # touch is over, display informations, and check if it matches some
        # known gesture.
        g = self.simplegesture(
            '',
            list(zip(touch.ud['line'].points[::2], touch.ud['line'].points[1::2]))
        )

        # use database to find the more alike gesture, if any
        g2 = self.gdb.find(g, minscore=0.70)
        if g2:
            if self._get_key_by_gesture(g2[1]) == self.letter:
                self.ponts += 10

        # erase the lines on the screen, this is a bit quick&dirty, since we
        # can have another touch event on the way...
        self.canvas.clear()
        self.sort_letter()

    def _get_key_by_gesture(self, g):
        for key, ges in gestures.items():
            if g == ges: return key

    def simplegesture(self, name, point_list):
        """
        A simple helper function
        """
        g = Gesture()
        g.add_stroke(point_list)
        g.normalize()
        g.name = name
        return g


class ABCGesture(App):
    def build(self):
        return GestureBoard()

if __name__ == '__main__':
    ABCGesture().run()

