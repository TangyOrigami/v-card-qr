import os
import qrcode
from PIL import Image

def list_files_in_directory(file_path):
    try:
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        if not files:
            return None
        return files
    except Exception as e:
        return f"An error occurred while listing files: {str(e)}"

def read_vcf_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as vcf_file:
            vcf_content = vcf_file.read()
        # Add a way to handle the image and cut out the xml

        return vcf_content
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def generate_qr_code(data, save_path, box_size, border):
    try:
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
                )
        qr.add_data(data)
        qr.make()

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(save_path)

        print(f"QR Code saved at: {save_path}")
    except Exception as e:
        print(f"Error generating QR Code: {str(e)}")

def set_directory():
    print('Enter path to vcards: ')
    file_path = input()
    if os.path.isdir(file_path):
        try:
            file_list = list_files_in_directory(file_path)

            for file_name in file_list:
                next_file = os.path.join(file_path, file_name)

                vcf_string = read_vcf_file(next_file)

                if not vcf_string.startswith("Error"):
                    print("Read VCF Successfully")

                    file_name_without_extension = os.path.splitext(file_name)[0]

                    qr_code_save_path = f"qr_codes/{file_name_without_extension}.png"

                    generate_qr_code(vcf_string, qr_code_save_path, box_size=1, border=1)
        except Exception as e:
            print(f"Error setting directory: {str(e)}")
    else:
        print('No such directory')

if __name__ == "__main__":
    print("Loading script...")
    set_directory()
