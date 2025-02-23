import pdfplumber
from typing import List, Optional
import os

def extract_text_from_pdf(file_path: str, page_numbers: Optional[List[int]] = None) -> dict:
    """
    Extract text from a PDF file using pdfplumber.
    
    Args:
        file_path (str): Path to the PDF file
        page_numbers (Optional[List[int]]): List of specific page numbers to extract (0-based).
                                          If None, extracts all pages.
    
    Returns:
        dict: Dictionary containing extracted text for each page and total page count
        
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        Exception: For other PDF processing errors
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    try:
        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            
            # If no specific pages requested, process all pages
            if page_numbers is None:
                page_numbers = range(total_pages)
            
            # Validate page numbers
            page_numbers = [p for p in page_numbers if 0 <= p < total_pages]
            
            result = {
                'total_pages': total_pages,
                'pages': {}
            }
            
            for page_num in page_numbers:
                page = pdf.pages[page_num]
                text = page.extract_text()
                if text:
                    result['pages'][page_num + 1] = text.strip()  # Convert to 1-based page numbers
                else:
                    result['pages'][page_num + 1] = ""
            
            return result

    except Exception as e:
        raise Exception(f"Error processing PDF: {str(e)}")

if __name__ == "__main__":
    try:
        # Example usage
        result = extract_text_from_pdf("file.pdf")
        
        print(f"Total pages in PDF: {result['total_pages']}")
        print("\nExtracted text by page:")
        for page_num, text in result['pages'].items():
            print(f"\nPage {page_num}:")
            print("-" * 40)
            print(text)
            
    except Exception as e:
        print(f"Error: {e}") 