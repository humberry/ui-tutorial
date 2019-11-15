# coding: utf-8

import ui


class MyButtonClass(ui.View):
    def __init__(self, label):
        self.color = "red"
        self.label = label
        self.label.text = "Push me"
        # touch event are limited to this area (left=100,top=100,right=200,bottom=200)
        self.x = 100
        self.y = 100
        self.height = 100
        self.width = 100

    def draw(self):
        # if the path is larger then 100x100 it will be clipped
        path = ui.Path.rect(0, 0, 100, 100)
        ui.set_color(self.color)
        path.fill()

    def touch_ended(self, touch):
        if self.color == "red":
            self.color = "blue"
            self.label.text = "again"
        else:
            self.color = "red"
            self.label.text = "Push me"
        self.set_needs_display()


class SpecialButton(object):
    def __init__(self):
        self.view = ui.load_view("SpecialButton")
        self.view.present("fullscreen")
        self.label = ui.Label(frame=(120, 100, 100, 100))
        self.btn = MyButtonClass(self.label)
        self.view.add_subview(
            self.btn
        )  # watch the order, first button and then the label
        self.view.add_subview(self.label)


SpecialButton()
