# pip install PyPDF2
# pip install pycryptodome

# Put all the files you want to unlock in the locked_files folder and the put your password in the code below. After running this code, you will find all the unlocked files in the unlocked_files folder.

import os
import PyPDF2

def remove_pdf_password(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, "rb") as input_file:
        reader = PyPDF2.PdfReader(input_file)
        
        if reader.is_encrypted:
            if not reader.decrypt(password):
                raise ValueError(f"Failed to decrypt: {input_pdf_path}")
        
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)
    
    print(f"Unlocked: {output_pdf_path}")

def unlock_all_pdfs_in_folder(input_folder, output_folder, password):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"unlocked_{filename}")
            try:
                remove_pdf_password(input_path, output_path, password)
            except Exception as e:
                print(f"Failed to unlock {filename}: {e}")

# Example usage
unlock_all_pdfs_in_folder(
    input_folder="locked_files",
    output_folder="unlocked_files",
    password="your_password_here"  # Replace with your actual password
)
