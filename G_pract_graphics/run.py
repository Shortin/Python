from PIL import Image,ImageOps

im = Image.open('pakmen.jpg')
# enhancer = ImageEnhance.Brightness(im)
img_border = ImageOps.expand(im, -100,fill = 'green').show()
factor = 1