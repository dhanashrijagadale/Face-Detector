import qrcode
import qrcode as qr
from PIL import Image
dhan=qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)
dhan.add_data("http://dhanashrijagadale.com/")
dhan.make(fit=True)
img=dhan.make_image(fill_color="Pink",back_color='white')
img.save("Dhanashri's  new .png")
