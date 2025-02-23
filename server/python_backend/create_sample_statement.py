from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime, timedelta
import os

def create_sample_statement(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Use a clear, monospaced font
    c.setFont("Courier", 24)
    c.drawString(50, height - 50, "Sample Bank Statement")
    
    c.setFont("Courier", 12)
    c.drawString(50, height - 80, "Statement Period: Feb 1, 2024 - Feb 29, 2024")
    c.drawString(50, height - 100, "Account Number: XXXX-XXXX-1234")
    
    # Add column headers
    y = height - 150
    c.setFont("Courier-Bold", 10)
    c.drawString(50, y, "Date")
    c.drawString(150, y, "Description")
    c.drawString(400, y, "Amount")
    c.drawString(500, y, "Balance")
    
    # Add transactions
    c.setFont("Courier", 10)
    y -= 20
    balance = 5000.00
    
    # Sample transactions
    transactions = [
        ("02/01/2024", "Direct Deposit - ACME Corp Salary", 3500.00),
        ("02/02/2024", "Amazon.com Purchase", -125.50),
        ("02/03/2024", "Grocery Store Purchase", -85.75),
        ("02/05/2024", "Netflix Subscription", -15.99),
        ("02/07/2024", "Restaurant Payment", -45.80),
        ("02/10/2024", "Gas Station", -40.00),
        ("02/12/2024", "Utility Bill Payment", -150.00),
        ("02/15/2024", "Medical Insurance", -200.00),
        ("02/18/2024", "Pharmacy Purchase", -35.50),
        ("02/20/2024", "Internet Bill", -75.00),
        ("02/23/2024", "Target Purchase", -95.30),
        ("02/25/2024", "Phone Bill", -80.00),
        ("02/28/2024", "Interest Earned", 2.50),
    ]
    
    for date, desc, amount in transactions:
        balance += amount
        
        # Ensure consistent spacing using monospace font
        c.drawString(50, y, date)
        # Limit description length to maintain readability
        desc = desc[:30].ljust(30)
        c.drawString(150, y, desc)
        
        # Format amounts with consistent spacing
        amount_str = f"${amount:>9,.2f}"
        balance_str = f"${balance:>9,.2f}"
        
        # Color code amounts
        if amount < 0:
            c.setFillColor(colors.red)
        else:
            c.setFillColor(colors.green)
        c.drawString(400, y, amount_str)
        
        c.setFillColor(colors.black)
        c.drawString(500, y, balance_str)
        
        y -= 20
    
    # Add summary
    y -= 40
    c.setFont("Courier-Bold", 12)
    c.drawString(50, y, "Monthly Summary")
    y -= 20
    
    total_income = sum(amount for _, _, amount in transactions if amount > 0)
    total_expenses = sum(amount for _, _, amount in transactions if amount < 0)
    
    c.setFont("Courier", 10)
    c.drawString(50, y, f"Total Income:   ${total_income:>9,.2f}")
    y -= 20
    c.drawString(50, y, f"Total Expenses: ${abs(total_expenses):>9,.2f}")
    y -= 20
    c.drawString(50, y, f"Net Change:     ${(total_income + total_expenses):>9,.2f}")
    
    c.save()

if __name__ == "__main__":
    create_sample_statement("sample_statement.pdf") 