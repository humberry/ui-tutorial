# coding: utf-8

import ui

class MultipleViews(ui.View):
	
    def __init__(self):
        self.view = ui.load_view('MultipleViews')
        self.view.present('fullscreen')
        self.add(None, text='First Run')

    def remove(self, sender):
        label = self.view['Label']
        if label != None:
            self.view.remove_subview(label)

    def add(self, sender, text='Labeltext'):
        label = ui.Label()
        label.name = 'Label'
        label.text = text
        self.view.add_subview(label)

MultipleViews()
