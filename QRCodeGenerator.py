# convert a url link to a QR code

import qrcode
import os

# get the url link
url = "https://www.jandlunderground.com/"

# create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3,
)

# clear qr data then add the url link to the QR code
qr.clear()
qr.add_data(url)
qr.make(fit=True)

# create the image
img = qr.make_image(fill_color="#654321", back_color="gray")
# save the image as a png file
img.save("jandl.png")

# open the image
os.startfile("jandl.png")

# end of program
