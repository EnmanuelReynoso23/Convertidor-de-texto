from docx import Document

class TXTConverter:
    def convert_to_txt(self, document_path):
        """
        Converts a document to TXT format.

        Args:
            document_path (str): The path to the document file.

        Returns:
            str: The converted document in TXT format.
        """
        # Load the document
        doc = Document(document_path)

        # Extract the text from the document
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        # Return the converted document
        return text