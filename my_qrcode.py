import qrcode


# in teminal type and install:
# pip install pillow
# pip install qrcode



x = qrcode.make("farhadkh736@gmail.com")
x.save("farhad.png")