# coding: utf-8

import ui

class Webbrowser(ui.View):
    def __init__(self):
        self.view = ui.load_view('Webbrowser')
        self.view.present('fullscreen')
        self.view.name = 'Webbrowser'
        self.view['textfield1'].text = 'http://www.google.com'
        self.view['textfield1'].delegate = self
        self.view['webview1'].delegate = self
        self.view['button1'].action = self.bt_back
        self.view['button2'].action = self.bt_forward
        self.view['button3'].action = self.bt_home
        self.view['button4'].action = self.bt_favorite
        self.view['webview1'].load_url(self.view['textfield1'].text)

    def bt_back(self, sender):
        self.view['textfield1'].text = ''
        self.view['webview1'].go_back()

    def bt_forward(self, sender):
        self.view['textfield1'].text = ''
        self.view['webview1'].go_forward()

    def bt_home(self, sender):
        self.view['textfield1'].text = 'http://www.google.com'
        self.view['webview1'].load_url(self.view['textfield1'].text)

    def bt_favorite(self, sender):
        self.view['textfield1'].text = 'Favorites'
        favorites = '<HTML><HEAD></HEAD><BODY><H1><P>'
        favorites += '<a href="http://www.yahoo.com">Yahoo</a> Websearch<br>'
        favorites += '<a href="http://www.cnn.com">CNN</a> News<br>'
        favorites += '<a href="http://www.picsearch.com">picsearch</a><br>'
        favorites += '</P></H1></BODY></HTML>'
        self.view['webview1'].load_html(favorites)

    def textfield_did_begin_editing(self, textfield):
        self.view['webview1'].stop()

    def textfield_did_end_editing(self, textfield):
        self.view['webview1'].load_url(self.view['textfield1'].text)

    def webview_did_start_load(self, webview):
        self.view['textfield1'].text_color = 'orange'

    def webview_did_finish_load(self, webview):
        self.view['textfield1'].text_color = 'black'

    def webview_did_fail_load(self, webview, error_code, error_msg):
        self.view['textfield1'].text_color = 'red'

Webbrowser()
