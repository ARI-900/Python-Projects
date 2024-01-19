from PIL import Image,ImageFilter

img1 = Image.open('Thamma.JPG')
img2 = Image.open('newpan.png')

# newImg = Image.blend(img2,img1,0.4)         # same size required for mearging 2 images
# newImg.show()


# img2.filter(ImageFilter.BoxBlur(60)).show()
# img2.filter((ImageFilter.EMBOSS)).show()
# img1.filter(ImageFilter.CONTOUR).show()
# img1.filter(ImageFilter.EDGE_ENHANCE).show()
# img1.filter(ImageFilter.DETAIL).show()
# img1.filter(ImageFilter.SHARPEN).show()
# img1.filter(ImageFilter.SMOOTH_MORE).show()

from PIL import Image,ImageDraw,ImageFont

image = Image.open('newp.png')
draw = ImageDraw.Draw(image)

size = 900,1400
str = "I am not done yet !!!"
font1 = ImageFont.truetype('arial.ttf',305,)

draw.text(size,str,'White',font=font1)
image.show()
