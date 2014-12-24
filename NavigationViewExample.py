# coding: utf-8

import ui

class NavView(ui.View):
    def __init__(self):
        root_view = ui.load_view()

        close = ui.ButtonItem()
        close.image = ui.Image.named('ionicons-close-24')
        close.action = self.bt_close
        root_view.left_button_items = [close]

        right = ui.ButtonItem()
        right.image = ui.Image.named('ionicons-arrow-right-b-24')
        right.action = self.bt_subview
        root_view.right_button_items = [right]
        
        self.nav_view = ui.NavigationView(root_view)
        self.nav_view.present(hide_title_bar=True)
        
    def bt_subview(self, sender):
        sub_view = ui.load_view('switchview1.pyui')
        sub_view.name = 'subview'
        sub_view['btn_Okay'].action = self.bt_action
        sub_view['btn_Cancel'].action = self.bt_action
        self.nav_view.push_view(sub_view)

    def bt_close(self, sender):
        self.nav_view.close()
        
    def bt_action(self, sender):
        print 'action from ' + sender.name

NavView()
