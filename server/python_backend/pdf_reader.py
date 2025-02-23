from pypdf import PdfReader # type: ignore
from typing import Dict, Optional
from pdf_text_extractor import extract_text_from_pdf

def read_pdf_metadata(file_path: str) -> Dict[str, Optional[str]]:
    """
    Read metadata from a PDF file.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        Dict[str, Optional[str]]: Dictionary containing the PDF metadata
        
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        Exception: For other PDF processing errors
    """
    try:
        reader = PdfReader(file_path)
        metadata = {
            'title': reader.metadata.get('/Title'),
            'author': reader.metadata.get('/Author'),
            'subject': reader.metadata.get('/Subject'),
            'creator': reader.metadata.get('/Creator'),
            'producer': reader.metadata.get('/Producer'),
            'creation_date': reader.metadata.get('/CreationDate'),
            'modification_date': reader.metadata.get('/ModDate'),
            'number_of_pages': len(reader.pages)
        }
        return metadata
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        metadata = read_pdf_metadata("file.pdf")
        print("PDF Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}")

    # New example usage
    try:
        result = extract_text_from_pdf("path/to/your/file.pdf")
        print("Extracted Text:")
        for page_number, text in result['pages'].items():
            print(f"Page {page_number}: {text}")
    except Exception as e:
        print(f"Error: {e}") 