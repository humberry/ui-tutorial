# coding: utf-8

import ui

v = ui.load_view('segmented-control')

def button_action(sender):
	if button1.selected_index == 0:
		v['text_label'].text = 'Hello'
	elif button1.selected_index == 1:
		v['text_label'].text ='World'

button1 = v['segmentedcontrol1']
button1.action = button_action

v.present('sheet')
