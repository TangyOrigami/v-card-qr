import os
import qrcode
from PIL import Image

def list_files_in_directory(file_path):
    try:
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        return files
    except Exception as e:
        return f"An error occurred while listing files: {str(e)}"

def read_vcf_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as vcf_file:
            vcf_content = vcf_file.read()
        return vcf_content
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def generate_qr_code(data, save_path, box_size, border):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
            )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

file_path = "/home/csaenz/vCard/qr-code/cards/"
vcf_string = read_vcf_file(file_path)

file_list = list_files_in_directory(file_path)

for file_name in file_list:
    next_file = os.path.join(file_path, file_name)

    vcf_string = read_vcf_file(next_file)

    if not vcf_string.startswith("Error"):
        print("Read VCF Successfully")

        file_name_without_extension = os.path.splitext(file_name)[0]

        qr_code_save_path = f"/home/csaenz/vCard/qr-code/qr-codes/{file_name_without_extension}.png"

        generate_qr_code(vcf_string, qr_code_save_path, box_size=3, border=1)

        print(f"QR Code saved at: {qr_code_save_path}")
    else:
        print(vcf_string)
