# coding: utf-8

import ui

class PopOverView(ui.View):
  view_main = None
  view_po = None 

  def __init__(self):
    PopOverView.view_main = ui.load_view('pop-over2')
    PopOverView.view_main.present('fullscreen')

  def quit(self, sender):
    PopOverView.view_main.touch_enabled = False 
    PopOverView.view_po = ui.load_view('po2')
    PopOverView.view_po.present('popover',popover_location=(400,400))

  def ask_user(self, sender):	#action method for both buttons (yes and no)
    PopOverView.view_po.close()
    if sender.name == 'yes':
      PopOverView.view_main.close()
    else:
      PopOverView.view_main.touch_enabled = True 

PopOverView()
