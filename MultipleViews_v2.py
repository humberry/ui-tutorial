# coding: utf-8

import ui

class MultipleViews(ui.View):
    def __init__(self):
        self.labelcounter = 0
        self.present()

    def did_load(self):
        self['bt_remove_label'].action = self.remove
        self['bt_add_label'].action = self.add
        self.add(None, text='First Run')

    def draw(self):
        print self.name
        print self.frame	#(0.0, 64.0, 1024.0, 704.0) with title // (0.0, 0.0, 1024.0, 704.0) no title
        print self.bounds	#(0.0, 0.0, 1024.0, 704.0)

    def remove(self, sender):
        label = self['Label']
        if label:
            self.remove_subview(label)
            self.labelcounter -= 1

    def add(self, sender, text='Labeltext'):
        self.labelcounter += 1
        label = ui.Label(name='Label')
        label.text = text
        label.x = label.y = self.labelcounter * 20
        self.add_subview(label)

v = ui.load_view()	# Custom View Class = MultipleViews

# Extra credit: modify remove() to delete the newest label first
#                              instead of the oldest label first.
