# coding: utf-8

import ui

def no_blank_lines(text):
    return '\n'.join([line.strip() for line in text.splitlines() if line])

def add_new_item(sender):
    tf_new_item = view['new_item']
    tv_shoppinglist = view['shoppinglist']
    tv_shoppinglist.text += '\n' + tf_new_item.text
    tv_shoppinglist.text = no_blank_lines(tv_shoppinglist.text)
    tf_new_item.text = ''

view = ui.load_view('layout')
view.present('fullscreen')
view['shoppinglist'].text = 'SHOPPINGLIST:\n'
