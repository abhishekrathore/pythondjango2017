__author__ = 'abhishekrathore'
from PIL import Image
from PIL import ImageEnhance

im = Image.open("demo.png")
# im.show()

print(im.format, im.size, im.mode)


enh = ImageEnhance.Contrast(im)
enh.enhance(2.3).show()

# box = (im.size[0]/2, 0, im.size[0], im.size[1]/2)
# region = im.crop(box)
# region.show()
# out = im.rotate(180)
# out.show()


out = im.transpose(Image.FLIP_LEFT_RIGHT)
# out.show()


# # out = im.convert('CMYK')
# out.show()
out.save("abc.png")

source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 120)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)

im.show()