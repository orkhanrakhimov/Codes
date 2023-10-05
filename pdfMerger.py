import PyPDF2
import os

# directory containing the PDF files
pdf_directory = "C:/Users/PC/Desktop/merger"

# List of PDF files to merge (in the desired order)
pdf_files = sorted([file for file in os.listdir(pdf_directory) if file.endswith(".pdf")])

if not pdf_files:
    print("No PDF files found for merging.")
else:
    merger = PyPDF2.PdfMerger()

    for file in pdf_files:
        pdf_path = os.path.join(pdf_directory, file)
        merger.append(pdf_path)

    output_file = "combinedPdf.pdf"
    merger.write(output_file)
    merger.close()

    print(f"Merged {len(pdf_files)} PDF files from {pdf_directory} into {output_file}.")
