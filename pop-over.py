# coding: utf-8

import ui, sys

answer = False
view_po = None 

def quit(sender):
  global view_po	#avoid global variables (I have to learn this...)
  def ask_user(sender):	#action method for both buttons (yes and no)
    global view_po, answer	#avoid global variables (I have to learn this...)
    if sender.name == 'yes':
      answer = True 
    else:
      answer = False
    view_po.close()
  view_po = ui.load_view('po')
  view_po.present('popover')

view = ui.load_view('pop-over')
view.present('fullscreen')
while True:
  if answer:
    view.close()
