# coding: utf-8

import ui

favorites_html = '''<HTML><HEAD></HEAD><BODY><H1><P>
    <a href="http://www.yahoo.com">Yahoo</a> Websearch<br>
    <a href="http://www.cnn.com">CNN</a> News<br>
    <a href="http://www.google.com/search?&tbm=nws&as_q=python+language">Google News (Python)</a><br>
    <a href="http://www.picsearch.com">picsearch</a><br>
    <a href="http://omz-forums.appspot.com/pythonista">Pythonista Forum</a><br>
</P></H1></BODY></HTML>'''

back = ui.ButtonItem()
back.image = ui.Image.named('ionicons-arrow-left-b-32')
forward = ui.ButtonItem()
forward.image = ui.Image.named('ionicons-arrow-right-b-32')

home = ui.ButtonItem()
home.image = ui.Image.named('ionicons-home-32')
favorite = ui.ButtonItem()
favorite.image = ui.Image.named('ionicons-bookmark-32')

class Webbrowser(ui.View):
    def __init__(self):
        back.action = self.bt_back
        forward.action = self.bt_forward
        home.action = self.bt_home
        favorite.action = self.bt_favorite
        self.left_button_items = [back, forward]
        self.right_button_items = [home, favorite]
        self.present()

    def did_load(self):
        self.name = 'Webbrowser'
        self['textfield1'].delegate = self['webview1'].delegate = self
        self.bt_home(None)

    def load_url(self, url=None):
        self['webview1'].load_url(url or self['textfield1'].text)

    def bt_back(self, sender):
        self['textfield1'].text = ''
        self['webview1'].go_back()

    def bt_forward(self, sender):
        self['textfield1'].text = ''
        self['webview1'].go_forward()

    def bt_home(self, sender):
        self['textfield1'].text = 'http://www.google.com'
        self.load_url()

    def bt_favorite(self, sender):
        self['textfield1'].text = 'Favorites'
        self['webview1'].load_html(favorites_html)

    def textfield_did_begin_editing(self, textfield):
        self['webview1'].stop()

    def textfield_did_end_editing(self, textfield):
        self.load_url()

    def webview_did_start_load(self, webview):
        self['textfield1'].text_color = 'orange'

    def webview_did_finish_load(self, webview):
        self['textfield1'].text_color = 'black'

    def webview_did_fail_load(self, webview, error_code, error_msg):
        self['textfield1'].text_color = 'red'

ui.load_view('Webbrowser')  # Custom View Class in the .pyui file must be set to Webbrowser
