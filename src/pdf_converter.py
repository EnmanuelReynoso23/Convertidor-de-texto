from pdf2image import convert_from_path

class PDFConverter:
    def convert_to_pdf(self, document_path, output_path):
        images = convert_from_path(document_path)
        for i, image in enumerate(images):
            image.save(f"{output_path}/page_{i+1}.pdf", "PDF")