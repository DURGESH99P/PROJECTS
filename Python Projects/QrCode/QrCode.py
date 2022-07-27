import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import image

qr = qrcode.QRCode(
    version=15, #15 means the version of the qrcode the higher the number the bigger the code image and complicated picture
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, # szie of the box where the qr code will be displayed 
    border=5, # it is the white part of image -- border in all 4 sides with white color
)

data = "https://www.youtube.com/"
# here you can post the path of the website of which qrcode you want to generate

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# These are optional parameters
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
# img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/test.png")

# now to save image use this
img.save("test1.png")


