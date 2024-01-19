from PIL import Image,ImageFilter,ImageDraw,ImageFont

# img = Image.open('newp.png')
# img.show()

# print(img.size)
# width,height = img.size
# print(f'Height: {height} width: {width}')
#
# print(img.height)
# print(img.width)
#
# print(img.format)



# img.thumbnail((300,300))
# img.save('newp2.png')
# print("Successfully save .....")


# img.rotate(180).show('Rotate Thamma')
# img.rotate(180).save('Rotate Thamma')


# area = (1713,0,3990,1908) #Tuple -> coordinate(starting,ending)
# img.crop(area).show()


# create Nex Image ---------------->
# img2 = Image.new('RGB',(600,400),color='navy').show() # Multiple modes are available, visit python documentation
'''Program 2'''
# size=(300,300)
# newimg = Image.new('RGB',size,'#ff00ee')
# newimg.save('myimg.png')


# # Mearge 2 img (Two images should be same size and mode)

# img1 = Image.open('newp2.png')
# img2 = Image.open('myimg.png')
# res = Image.blend(img1,img2,0.5)
# res.show("Hero")

# Image FIlter required (ImageFilter)
# res = img.filter(ImageFilter.Filter)  #Edge Enhancemode,contour,Emboss,Detail,smooth
# res.show('temp.png')

# Image Text required (ImageDraw)

# img = Image.open('newp.png')
# res = ImageDraw.Draw(img)
# font = ImageFont.truetype('arial.ttf',290,)
# res.text((370,1810),'Khachhor Biral',font=font,fill='navy')
# img.show()
