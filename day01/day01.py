#往图片右上角添加红色数字
#2018年03月13日18:12:27
from PIL import Image, ImageDraw, ImageFont

im = Image.open('dingchun.JPEG')
im.show()
drawAvatar = ImageDraw.Draw(im)
xSize, ySize = im.size
fontsize = min(xSize, ySize) // 12
myFont = ImageFont.truetype('HYXiaRiTiW.ttf', fontsize)
drawAvatar.text([0.9*xSize, 0.1*ySize-fontsize], text='1', fill='red', font=myFont)
im.show()
im.save('result.JPEG')