import sys
import json
import re
from datetime import datetime
import pytesseract
from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import cv2

def preprocess_image(image):
    # Convert PIL image to OpenCV format
    image = np.array(image)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(
        gray, 
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,  # Block size
        2    # C constant
    )
    
    # Denoise
    denoised = cv2.fastNlMeansDenoising(binary)
    
    # Apply dilation to connect text components
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,1))
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    
    # Scale up the image (can improve OCR accuracy)
    scale_factor = 2
    scaled = cv2.resize(dilated, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    
    return scaled

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    extracted_text = []
    for image in images:
        # Preprocess the image
        processed_image = preprocess_image(image)
        
        # Configure Tesseract for table data
        custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
        
        # Perform OCR with custom configuration
        text = pytesseract.image_to_string(
            processed_image,
            config=custom_config,
            lang='eng'
        )
        extracted_text.append(text)
    
    return '\n'.join(extracted_text)

def parse_amount(amount_str):
    # Remove currency symbols and commas, then convert to float
    amount_str = re.sub(r'[^\d.-]', '', amount_str)
    try:
        return float(amount_str)
    except ValueError:
        return 0.0

def categorize_transaction(description):
    # Simple rule-based categorization
    description = description.lower()
    
    categories = {
        'salary': ['salary', 'payroll', 'direct deposit'],
        'food': ['restaurant', 'cafe', 'grocery', 'food'],
        'transport': ['uber', 'lyft', 'taxi', 'transport', 'gas', 'fuel'],
        'utilities': ['electricity', 'water', 'internet', 'phone'],
        'shopping': ['amazon', 'walmart', 'target', 'store'],
        'entertainment': ['netflix', 'spotify', 'movie', 'theatre'],
        'healthcare': ['medical', 'doctor', 'pharmacy', 'hospital'],
        'housing': ['rent', 'mortgage', 'maintenance']
    }
    
    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    
    return 'other'

def clean_amount(amount_str):
    """Clean and parse amount string, handling OCR imperfections."""
    # Replace common OCR mistakes for currency symbols
    amount_str = amount_str.replace('§', '$').replace('S$', '$')
    
    # Remove all spaces
    amount_str = amount_str.replace(' ', '')
    
    # Handle negative amounts with various formats
    amount_str = amount_str.replace('--', '-')
    
    # Extract the number, handling negative signs
    matches = re.findall(r'[-+]?\d[,\d]*\.?\d*', amount_str)
    if not matches:
        return 0.0
    
    # Take the first match (transaction amount) rather than the last (balance)
    amount_str = matches[0]
    
    # Remove commas and convert to float
    try:
        return float(amount_str.replace(',', ''))
    except ValueError:
        return 0.0

def extract_amount(line):
    """Extract transaction amount from a line, handling OCR imperfections."""
    # Look for amount patterns with currency symbols
    # Pattern specifically looks for transaction amounts (not balance)
    # Matches both positive and negative amounts with proper spacing
    patterns = [
        r'[\$§][\s]*[-][\s]*\d+,?\d*\.\d{2}(?=\s)',  # Negative amounts
        r'[\$§][\s]*\d+,?\d*\.\d{2}(?=\s)',          # Positive amounts
    ]
    
    for pattern in patterns:
        matches = list(re.finditer(pattern, line))
        if matches:
            # Get the first match and clean it
            amount_str = matches[0].group(0)
            amount_str = amount_str.replace('§', '$').replace('S$', '$')
            amount_str = amount_str.replace(' ', '')
            
            # Extract the numeric part
            number_match = re.search(r'[-]?\d[,\d]*\.\d{2}', amount_str)
            if number_match:
                try:
                    # Handle negative amounts
                    amount = float(number_match.group(0).replace(',', ''))
                    # If the amount string contains a minus sign, make sure it's negative
                    if '-' in amount_str:
                        amount = -abs(amount)
                    return amount
                except ValueError:
                    continue
    
    return None

def clean_description(desc):
    """Clean up description text."""
    # Remove amount and balance information
    desc = re.sub(r'[\$§][\s]*[-]?\d+,?\d*\.\d{2}.*$', '', desc)
    
    # Remove multiple spaces
    desc = ' '.join(desc.split())
    
    # Remove common OCR artifacts
    desc = desc.replace('|', '').replace('_', '')
    
    # Remove trailing punctuation
    desc = desc.rstrip('.,:-')
    
    return desc.strip()

def process_statement(text):
    """Process the OCR output text into structured data."""
    # Split text into lines and clean up
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    transactions = []
    total_income = 0
    total_expenses = 0
    
    # Find the start of transactions (after headers)
    start_idx = 0
    for i, line in enumerate(lines):
        if re.search(r'Date.*Description.*Amount.*Balance', line, re.IGNORECASE):
            start_idx = i + 1
            break
    
    # Process transaction lines
    current_date = None
    current_description = []
    current_amount = None
    
    for line in lines[start_idx:]:
        # Skip summary section
        if 'Monthly Summary' in line:
            break
            
        # Look for date pattern
        date_match = re.search(r'(\d{2}/\d{2}/\d{4})', line)
        
        if date_match:
            # If we have a previous transaction, save it
            if current_date and current_description and current_amount is not None:
                desc_text = clean_description(' '.join(current_description))
                # Skip if description is empty or just contains "Balance"
                if desc_text and not desc_text.lower() == 'balance':
                    transaction = {
                        'date': datetime.strptime(current_date, '%m/%d/%Y').isoformat(),
                        'description': desc_text,
                        'amount': abs(current_amount),
                        'category': categorize_transaction(desc_text),
                        'type': 'income' if current_amount > 0 else 'expense'
                    }
                    transactions.append(transaction)
                    
                    # Update totals
                    if current_amount > 0:
                        total_income += current_amount
                    else:
                        total_expenses += abs(current_amount)
            
            # Start new transaction
            current_date = date_match.group(1)
            current_description = []
            current_amount = extract_amount(line)
            
            # Extract description
            desc_part = line[date_match.end():].strip()
            if desc_part:
                current_description.append(desc_part)
        
        elif current_date and current_amount is None:
            # Try to find amount in this line
            current_amount = extract_amount(line)
            if current_amount is None:
                # If no amount found, treat as additional description
                current_description.append(line.strip())
        
        elif current_date:
            # Additional description line
            current_description.append(line.strip())
    
    # Add the last transaction if exists
    if current_date and current_description and current_amount is not None:
        desc_text = clean_description(' '.join(current_description))
        if desc_text and not desc_text.lower() == 'balance':
            transaction = {
                'date': datetime.strptime(current_date, '%m/%d/%Y').isoformat(),
                'description': desc_text,
                'amount': abs(current_amount),
                'category': categorize_transaction(desc_text),
                'type': 'income' if current_amount > 0 else 'expense'
            }
            transactions.append(transaction)
            
            # Update totals
            if current_amount > 0:
                total_income += current_amount
            else:
                total_expenses += abs(current_amount)
    
    # If no transactions found, try to extract summary information
    if not transactions:
        for line in lines:
            if 'Total Income' in line:
                amount = extract_amount(line)
                if amount is not None:
                    total_income = abs(amount)  # Summary amounts should be positive
            elif 'Total Expenses' in line:
                amount = extract_amount(line)
                if amount is not None:
                    total_expenses = abs(amount)  # Summary amounts should be positive
    
    return {
        'totalIncome': total_income,
        'totalExpenses': total_expenses,
        'transactions': transactions
    }

def process_pdf(file_path):
    # This is a placeholder implementation
    # In a real implementation, you would use libraries like pdfplumber or PyPDF2 to extract text
    # and implement proper parsing logic
    
    # Return dummy data for now
    return {
        "totalIncome": 5000.00,
        "totalExpenses": 3000.00,
        "transactions": [
            {
                "date": datetime.now().isoformat(),
                "description": "Sample Income",
                "amount": 5000.00,
                "category": "Salary",
                "type": "income"
            },
            {
                "date": datetime.now().isoformat(),
                "description": "Sample Expense",
                "amount": 3000.00,
                "category": "Rent",
                "type": "expense"
            }
        ]
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "File path not provided"}))
        sys.exit(1)
        
    try:
        result = process_pdf(sys.argv[1])
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1) 