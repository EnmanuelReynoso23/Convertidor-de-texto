from docx import Document

class DOCXConverter:
    def convert_to_docx(self, input_file, output_file):
        document = Document()
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                document.add_paragraph(line.strip())
        document.save(output_file)