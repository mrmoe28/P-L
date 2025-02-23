import { useState } from 'react'
import PDFUploader from '../PDFUploader'
import StatementViewer from '../StatementViewer'

const HomePage = () => {
  const [currentStatement, setCurrentStatement] = useState<string | null>(null)

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Bank Statement Analyzer</h1>
              <p className="mt-1 text-sm text-gray-500">
                Convert your bank statements into detailed financial reports
              </p>
            </div>
            {/* Add any header actions here */}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section - Show only when no statement is uploaded */}
        {!currentStatement && (
          <div className="text-center mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              Welcome to Bank Statement Analyzer
            </h2>
            <p className="text-gray-600 max-w-2xl mx-auto">
              Upload your bank statement PDF and let our AI-powered system analyze your transactions,
              categorize expenses, and generate detailed financial reports.
            </p>
          </div>
        )}

        {/* Main Grid */}
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-2">
          {/* Upload Section */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="mb-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-2">
                Upload Statement
              </h2>
              <p className="text-sm text-gray-500">
                Supported format: PDF bank statements
              </p>
            </div>
            <PDFUploader onUploadSuccess={setCurrentStatement} />
          </div>

          {/* Analysis Section */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="mb-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-2">
                Statement Analysis
              </h2>
              <p className="text-sm text-gray-500">
                View your processed financial data
              </p>
            </div>
            <StatementViewer statementId={currentStatement} />
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-16">
          <h2 className="text-2xl font-semibold text-gray-900 mb-8 text-center">
            Key Features
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="bg-white rounded-lg shadow-sm p-6">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                Smart OCR Processing
              </h3>
              <p className="text-gray-500 text-sm">
                Advanced OCR technology accurately extracts data from your bank statements
              </p>
            </div>

            {/* Feature 2 */}
            <div className="bg-white rounded-lg shadow-sm p-6">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                Automatic Categorization
              </h3>
              <p className="text-gray-500 text-sm">
                AI-powered transaction categorization for better financial insights
              </p>
            </div>

            {/* Feature 3 */}
            <div className="bg-white rounded-lg shadow-sm p-6">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                Detailed Reports
              </h3>
              <p className="text-gray-500 text-sm">
                Generate comprehensive financial reports with income and expense analysis
              </p>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <p className="text-center text-sm text-gray-500">
            © {new Date().getFullYear()} Bank Statement Analyzer. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  )
}

export default HomePage 