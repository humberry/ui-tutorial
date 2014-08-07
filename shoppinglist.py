# coding: utf-8

import ui

def add_new_item(sender):
  tf_new_item = view['new_item']
  tv_shoppinglist = view['shoppinglist']
  tv_shoppinglist.text += tf_new_item.text + '\n'
  tf_new_item.text = ''

view = ui.load_view('shoppinglist')
view.present('fullscreen')
