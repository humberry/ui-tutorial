# coding: utf-8

import ui

class MultipleViews(object):
    def __init__(self):
        self.view = ui.load_view('MultipleViews')
        self.view.present('fullscreen')
        self.add(None, text='First Run')

    def remove(self, sender):
        label = self.view['Label']
        if label:
            self.view.remove_subview(label)

    def add(self, sender, text='Labeltext'):
        label = ui.Label(name='Label')
        label.text = text
        self.view.add_subview(label)

MultipleViews()
