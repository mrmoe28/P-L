import { useState, useCallback } from 'react'
import { useMutation } from '@tanstack/react-query'
import axios from 'axios'

interface PDFUploaderProps {
  onUploadSuccess: (statementId: string) => void
}

const PDFUploader = ({ onUploadSuccess }: PDFUploaderProps) => {
  const [isDragging, setIsDragging] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const uploadMutation = useMutation({
    mutationFn: async (file: File) => {
      const formData = new FormData()
      formData.append('file', file)
      const response = await axios.post('http://localhost:3000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      return response.data
    },
    onSuccess: (data) => {
      onUploadSuccess(data.statementId)
      setError(null)
    },
    onError: (error: Error) => {
      setError(error.message)
    },
  })

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setIsDragging(true)
    } else if (e.type === 'dragleave') {
      setIsDragging(false)
    }
  }, [])

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setIsDragging(false)

    const files = Array.from(e.dataTransfer.files)
    const pdfFile = files.find(file => file.type === 'application/pdf')

    if (pdfFile) {
      uploadMutation.mutate(pdfFile)
    } else {
      setError('Please upload a PDF file')
    }
  }, [uploadMutation])

  const handleFileInput = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file && file.type === 'application/pdf') {
      uploadMutation.mutate(file)
    } else {
      setError('Please upload a PDF file')
    }
  }, [uploadMutation])

  return (
    <div
      className={`border-2 border-dashed rounded-lg p-6 text-center ${
        isDragging ? 'border-primary-500 bg-primary-50' : 'border-gray-300'
      }`}
      onDragEnter={handleDrag}
      onDragOver={handleDrag}
      onDragLeave={handleDrag}
      onDrop={handleDrop}
    >
      <div className="space-y-4">
        <div className="flex items-center justify-center">
          <svg
            className="w-12 h-12 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
          </svg>
        </div>
        
        <div className="text-gray-600">
          <p className="font-medium">
            Drag and drop your bank statement PDF here, or{' '}
            <label className="text-primary-600 hover:text-primary-500 cursor-pointer">
              browse
              <input
                type="file"
                className="hidden"
                accept=".pdf"
                onChange={handleFileInput}
              />
            </label>
          </p>
          <p className="text-sm">Only PDF files are supported</p>
        </div>

        {uploadMutation.isPending && (
          <div className="text-primary-600">Uploading...</div>
        )}

        {error && (
          <div className="text-red-600">{error}</div>
        )}
      </div>
    </div>
  )
}

export default PDFUploader 