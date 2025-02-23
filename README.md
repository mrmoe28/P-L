# PDF Bank Statement Analyzer

A full-stack application that converts bank statements from PDF format into structured profit and loss statements using OCR and AI-powered parsing.

## Features

- PDF upload and processing
- OCR text extraction
- Intelligent transaction categorization
- Income and expense tracking
- Beautiful and responsive UI
- Real-time updates using React Query

## Tech Stack

### Frontend

- React.js with TypeScript
- Tailwind CSS for styling
- React Query for state management
- Axios for API requests

### Backend

- Node.js with Express
- MongoDB for data storage
- Python for PDF processing
- Tesseract OCR for text extraction
- OpenCV for image preprocessing

## Prerequisites

- Node.js (v14 or higher)
- Python 3.8 or higher
- MongoDB
- Tesseract OCR
- poppler-utils (for pdf2image)

### Installing Prerequisites

#### macOS

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install tesseract
brew install poppler
brew install mongodb-community

# Start MongoDB
brew services start mongodb-community
```

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd pdf-statement-analyzer
```

1. Install frontend dependencies:

```bash
cd client
npm install
```

1. Install backend dependencies:

```bash
cd ../server
npm install
```

1. Install Python dependencies:

```bash
cd python_backend
pip install -r requirements.txt
```

1. Create necessary directories:

```bash
mkdir uploads
```

1. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

1. Start the frontend development server:

```bash
cd client
npm run dev
```

1. Start the backend server:

```bash
cd server
npm start
```

The application will be available at:

- Frontend: <http://localhost:5173>
- Backend: <http://localhost:3000>

## Usage

1. Open the application in your web browser
2. Click the upload button or drag and drop a PDF bank statement
3. Wait for the processing to complete
4. View the analyzed statement with categorized transactions and totals

## Development

- Frontend code is in the `client` directory
- Backend Node.js code is in the `server` directory
- Python PDF processing code is in the `server/python_backend` directory

## Contributing

1. Fork the repository
1. Create a feature branch
1. Commit your changes
1. Push to the branch
1. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
