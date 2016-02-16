# coding: utf-8

import ui, photos, console

class MyPictureView(ui.View):
    def __init__(self, width, height):
        self.frame = (0,0,width,height)
        self.iwidth = 200.0
        self.iheight = 200.0
        framesize = 10
        iw = self.iwidth - 2 * framesize
        ih = self.iheight - 2 * framesize
        
        ratio = ih / iw
        self.img = []
        self.imgcount = min(photos.get_count(), 100)
        console.hud_alert('Please wait while {} photos are loading...'.format(self.imgcount))
        for i in xrange(self.imgcount):
            s = photos.get_metadata(i)
            if s['filename'][-3:] == 'MOV':     #skip movies
                self.img.append(None)
                continue
            img = ui.Image.from_data(photos.get_image(i,raw_data=True))
            w, h = img.size
            rat = h / w
            x_ratio = 1.0
            y_ratio = 1.0
            x = framesize
            y = framesize
            
            if ratio < 1:      #landscape canvas
                if rat <= ratio:     #full width
                    y = ((ih - iw * rat) / 2) + framesize
                    y_ratio = iw * rat / ih
                else:                #full height
                    x = ((iw - ih / rat) / 2) + framesize
                    x_ratio = ih / rat / iw
            elif ratio > 1:    #portrait canvas
                if rat > ratio:      #full height
                    x = ((iw - ih / rat) / 2) + framesize
                    x_ratio = ih / rat / iw
                else:                #full width
                    y = ((ih - iw * rat) / 2) + framesize
                    y_ratio = iw * rat / ih
            else:              #cubic canvas
                if rat < 1:          #full width
                    y = ((ih - iw * rat) / 2) + framesize
                    y_ratio = iw * rat / ih
                elif rat > 1:        #full height
                    x = ((iw - ih / rat) / 2) + framesize
                    x_ratio = ih / rat / iw
                else:                #cubic
                    pass             #x_ratio = y_ratio = 1.0
            with ui.ImageContext(self.iwidth, self.iheight) as ctx:
                img.draw(x,y,iw * x_ratio,ih * y_ratio)
                self.img.append(ctx.get_image())
            
    def draw(self):
        i = 0
        if self.imgcount < 100:
            endrow = self.imgcount / 10 + 1
        else:
            endrow = 10
        for row in xrange(endrow):
            for column in xrange(10):
                if i == self.imgcount:
                    break
                if self.img[i]:
                    x = column * self.iwidth
                    y = row * self.iheight
                    self.img[i].draw(x,y,self.iwidth,self.iheight)
                i += 1
        
class MiniPhotoView(ui.View):
    def __init__(self):
        self.view = ui.View(background_color='lightyellow')
        self.view.name = 'MiniPhotoView'
        scrollview1 = ui.ScrollView()
        scrollview1.name = 'scrollview1'
        scrollview1.flex = 'WH'
        scrollview1.content_size = (2000,2000)
        self.view.add_subview(scrollview1)
        self.view.present('full_screen')
        self.sv1 = self.view['scrollview1']
        width, height = self.sv1.content_size
        self.sv1.add_subview(MyPictureView(width,height))

if photos.get_count():
    MiniPhotoView()
else:
    print('Sorry no access or no pictures.')