import PyPDF2
import os

def concatenate_pdfs(directory, name, output_filename):
    # List all files in the given directory
    files = os.listdir(directory)

    # Filter the list to only include files ending with .pdf and containing the specified name
    pdf_files = [file for file in files if file.lower().endswith('.pdf') and name.lower() in file.lower()]

    # If you want to sort the PDF files by name
    pdf_files.sort()

    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Append each PDF to the merger object
    for pdf in pdf_files:
        with open(os.path.join(directory, pdf), 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    # Write the merged PDF to the output file
    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

# Prompt the user for the desired string
name_string = input("Enter the name string to search for in PDF filenames: ")

directory_path = "./"  # Current directory
output_file = f"{name_string}_fulldoc.pdf"
concatenate_pdfs(directory_path, name_string, output_file)

