import os
import qrcode
import vobject

path = '/home/csaenz/vCard/qr-code'

vcf_directory = os.path.join(path, 'cards')
vcf_files = [f for f in os.listdir(vcf_directory) if f.endswith('.vcf')]

for vcf_file in vcf_files:
    vcf_path = os.path.join(vcf_directory, vcf_file)

    # Parse the vCard file
    with open(vcf_path, 'r') as f:
        vcard_data = f.read()
        vcard = vobject.readOne(vcard_data)

    # Extract information from the vCard
    full_name = vcard.fn.value if vcard.fn else 'Unknown'

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(str(vcard))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a directory
    img.save(os.path.join(path, 'qr-codes', f'{full_name}_qr_code.png'))

