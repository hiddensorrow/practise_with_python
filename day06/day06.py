from PIL import Image
import os

path = os.path.join(os.path.dirname(__file__), 'imgs')
for filename in os.listdir(path):
    if '.jpg' in filename:
        print(filename)
        filename = os.path.join(path, filename)
        img = Image.open(filename)
        # img.show()
        # print(img.size)
        img = img.resize((1136, 640), Image.ANTIALIAS)
        # img.show()
        print(img.size)