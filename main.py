import os
import qrcode

path = '/home/csaenz/vCard/qr-code/cards'

onlyfiles = [f for f in os.listdir(path)]
print(onlyfiles)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

print(path+'/'+onlyfiles[0])

for entry in onlyfiles:
    entry = path+'/'+entry
    qr.add_data(entry)

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
