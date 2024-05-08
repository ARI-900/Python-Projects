import qrcode as qr
from PIL import Image    # not required

qrcode =qr.QRCode(version=1,
                  error_correction=qr.constants.ERROR_CORRECT_H,
                  box_size=10,border=4)
qrcode.add_data("https://www.youtube.com/")
qrcode.make(fit=True)
img = qrcode.make_image(fill_color="red",back_color='blue')
img.save("YouTue-QR.png")



# first process easy step
'''
import qrcode as qr

def main():
    qrcode = qr.make("https://www.youtube.com/")
    qrcode.save("YouTube_QRCODE.png")
main()

'''