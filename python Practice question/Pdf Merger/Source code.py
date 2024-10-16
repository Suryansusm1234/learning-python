from pypdf import PdfWriter, PdfReader

def merge_pdfs(input_paths, output_path):
    merger = PdfWriter()

    for path in input_paths:
        with open(path, 'rb') as file:
            reader = PdfReader(file)
            if reader.is_encrypted:
                print(f"The file {reader} was found to be encrypted")
                password = input("Enter the file password:-")
                try:
                    reader.decrypt(password)  # Try to decrypt if encrypted
                except:
                    print(f"Failed to decrypt {path}. Skipping this file.")
                    continue
            merger.append(reader)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print("PDF files merged successfully")

# Paths to your input PDFs
input_paths = []
a  = int(input("Enter the number of pdf file You want to merge:-"))
for i in range(a):
    file = input("Enter the file path:-")
    input_paths.append(file)
    
# Path for the output PDF
path = input("Enter the path or the name of the output file:-")
output_path = path

merge_pdfs(input_paths, output_path)