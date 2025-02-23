import os
import json
from create_sample_statement import create_sample_statement
from process_pdf import extract_text_from_pdf, process_statement

def test_pdf_processing():
    # Create a sample statement
    sample_pdf = "sample_statement.pdf"
    create_sample_statement(sample_pdf)
    
    try:
        # Extract text from the PDF
        print("Extracting text from PDF...")
        extracted_text = extract_text_from_pdf(sample_pdf)
        print("\nExtracted Text Sample:")
        print("----------------------")
        print(extracted_text[:500] + "...\n")
        
        # Process the statement
        print("Processing statement...")
        result = process_statement(extracted_text)
        
        # Print results
        print("\nProcessing Results:")
        print("------------------")
        print(f"Total Income: ${result['totalIncome']:.2f}")
        print(f"Total Expenses: ${result['totalExpenses']:.2f}")
        print(f"\nTransactions found: {len(result['transactions'])}")
        
        print("\nSample Transactions:")
        print("-------------------")
        for i, transaction in enumerate(result['transactions'][:3], 1):
            print(f"{i}. Date: {transaction['date']}")
            print(f"   Description: {transaction['description']}")
            print(f"   Amount: ${transaction['amount']:.2f}")
            print(f"   Category: {transaction['category']}")
            print(f"   Type: {transaction['type']}\n")
        
        # Clean up
        if os.path.exists(sample_pdf):
            os.remove(sample_pdf)
            
        return True
        
    except Exception as e:
        print(f"\nError during processing: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting PDF processing test...\n")
    success = test_pdf_processing()
    print("\nTest completed successfully!" if success else "\nTest failed!") 