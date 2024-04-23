import os
from PyPDF2 import PdfMerger, PdfReader
from natsort import natsorted

def merge_pdfs(directory='.'):
    merger = PdfMerger()
    
    pdf_files = []
    
    directory_name = os.path.basename(os.path.abspath(directory))
    output_filename = f'{directory_name}_Merged.pdf'

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.pdf') and filename != output_filename:
                filepath = os.path.join(root, filename)
                print(f"Collecting {filepath}...")
                pdf_files.append(filepath)

    pdf_files = natsorted(pdf_files)
    
    for filepath in pdf_files:
        print(f"Merging {filepath}... { len(merger.pages)}")
        merger.append(filepath)
        filename = os.path.basename(filepath)
        bookmark_title = filename[:-4]  # Remove the '.pdf' extension
        # Get the number of pages in the merged PDF so far
        num_pages = sum(len(PdfReader(filepath).pages) for filepath in pdf_files[:-1])
        merger.add_outline_item(bookmark_title, len(merger.pages) - len(PdfReader(filepath).pages))  # Add bookmark for the appended file
        
    if os.path.exists(output_filename):
        os.remove(output_filename)  # Remove the existing merged PDF file
    
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)
    
    print(f"All PDFs merged into '{output_filename}'.")

if __name__ == "__main__":
    merge_pdfs()
