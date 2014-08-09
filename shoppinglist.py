# coding: utf-8

import ui

def add_new_item(sender):
  tf_new_item = view['new_item']
  tv_shoppinglist = view['shoppinglist']
  new_item = tf_new_item.text.strip()
  if new_item:  # avoid adding blank lines
      tv_shoppinglist.text += new_item + '\n'
      tf_new_item.text = ''

view = ui.load_view('shoppinglist')
view.present()
