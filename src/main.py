from  docx_converter import DOCXConverter
from  txt_converter import TXTConverter
from file_utils import get_file_extension, create_output_directory
from pdf_converter import PDFConverter



def main():
    # Get the input file path and desired output format from the user
    input_file = input("Enter the path of the document file: ")
    output_format = input("Enter the desired output format (pdf/docx/txt): ")



    # Create the output directory if it doesn't exist
    create_output_directory()

    # Convert the document to the desired format
    if output_format == "pdf":
        converter = PDFConverter()
        converter.convert_to_pdf(input_file)
    elif output_format == "docx":
        converter = DOCXConverter()
        converter.convert_to_docx(input_file)
    elif output_format == "txt":
        converter = TXTConverter()
        converter.convert_to_txt(input_file)
    else:
        print("Invalid output format. Only pdf, docx, and txt are supported.")

if __name__ == "__main__":
    main()
    
import sys

print(sys.path)