import ui, Image, ImageDraw, ImageFont, io
from PIL import Image as ImageP

#style = 'sheet'
style = 'fullscreen'

font = ImageFont.truetype("Helvetica", 30)

def Img2ui(ip):
    with io.BytesIO() as bIO:
        ip.save(bIO, 'PNG')
        img = ui.Image.from_data(bIO.getvalue())
        img = img.with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
        return img

class MyView (ui.View):
    def __init__(self):
        self.background_color = 'lightgreen'
        self.draw_count = 0
        self.layout_count = 0

    def will_close(self):
        self.background_color = 'lightgrey'
        print("You can't see a lightgrey background, because the view is closed.")

    def draw(self):
        self.draw_count += 1
        img = Image.open('iob:arrow_expand_256')
        draw = ImageDraw.Draw(img)
        draw.line((0, 0) + img.size, fill=128, width=5)
        draw.line((0, img.size[1], img.size[0], 0), fill=128, width=5)
        fx, fy = draw.textsize('Hello',font=font)
        draw.text((img.size[0]/2-fx/2,img.size[1]/2-fy/2),'Hello',font=font,fill='red')
        img = Img2ui(img).draw(0, 0, self.width, self.height)
        print(f'[draw] counter = {self.draw_count}')

    def layout(self):
        orientation = None
        x, y = self.center
        if x > y:
          orientation = 'landscape'
        else:
          orientation = 'portrait'
        self.layout_count += 1
        print(f'[layout] counter = {self.layout_count}, mode = {style}, orientation = {orientation}')
        #In fullscreen mode orientation (portrait/landscape) is tracked

    def touch_began(self, touch):
        self.background_color = 'lightblue'

    def touch_ended(self, touch):
        self.background_color = 'yellow'

v = MyView()
v.present(style)

'''
<start>
[layout] counter = 1, mode = sheet, orientation = portrait
[layout] counter = 2, mode = sheet, orientation = portrait
[draw] counter = 1
<view is visible>
<touch_begin>
[draw] counter = 2
<touch_ended>
[draw] counter = 3
<will_close>
You can't see a lightgrey background, because the view is closed.
[draw] counter = 4
'''

'''
<start>
[layout] counter = 1, mode = fullscreen, orientation = portrait
[layout] counter = 2, mode = fullscreen, orientation = portrait
[draw] counter = 1
<view is visible>
<rotating screen >>> layout>
[layout] counter = 3, mode = fullscreen, orientation = landscape
[draw] counter = 2
<will_close>
You can't see a lightgrey background, because the view is closed.
[draw] counter = 3
'''
