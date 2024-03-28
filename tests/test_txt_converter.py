import unittest
from src.txt_converter import TXTConverter

class TestTXTConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TXTConverter()

    def test_convert_to_txt(self):
        # Test conversion from document to TXT format
        document_path = "path/to/document.docx"
        output_path = "path/to/output.txt"
        self.converter.convert_to_txt(document_path, output_path)
        
        # Add assertions to check if the conversion was successful
        # For example, you can check if the output file exists and has the expected content

if __name__ == "__main__":
    unittest.main()