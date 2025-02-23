import express from 'express'
import cors from 'cors'
import multer from 'multer'
import path from 'path'
import { PythonShell } from 'python-shell'
import mongoose from 'mongoose'
import dotenv from 'dotenv'

dotenv.config()

const app = express()
const port = process.env.PORT || 3000

// Middleware
app.use(cors())
app.use(express.json())

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/pdf-analyzer')

// Configure multer for file upload
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/')
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname))
  }
})

const upload = multer({
  storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype === 'application/pdf') {
      cb(null, true)
    } else {
      cb(new Error('Only PDF files are allowed'))
    }
  }
})

// Statement Schema
const statementSchema = new mongoose.Schema({
  filename: String,
  totalIncome: Number,
  totalExpenses: Number,
  transactions: [{
    date: Date,
    description: String,
    amount: Number,
    category: String,
    type: {
      type: String,
      enum: ['income', 'expense']
    }
  }],
  createdAt: {
    type: Date,
    default: Date.now
  }
})

const Statement = mongoose.model('Statement', statementSchema)

// Routes
app.post('/api/upload', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) {
      throw new Error('No file uploaded')
    }

    const options = {
      mode: 'text',
      pythonPath: 'python3',
      pythonOptions: ['-u'],
      scriptPath: './python_backend',
      args: [req.file.path]
    }

    const results = await PythonShell.run('process_pdf.py', options)
    const parsedData = JSON.parse(results[0])

    const statement = new Statement({
      filename: req.file.filename,
      ...parsedData
    })

    await statement.save()

    res.json({
      statementId: statement._id,
      message: 'File processed successfully'
    })
  } catch (error) {
    console.error('Error processing file:', error)
    res.status(500).json({
      error: 'Error processing file'
    })
  }
})

app.get('/api/statements/:id', async (req, res) => {
  try {
    const statement = await Statement.findById(req.params.id)
    if (!statement) {
      return res.status(404).json({ error: 'Statement not found' })
    }
    res.json(statement)
  } catch (error) {
    console.error('Error fetching statement:', error)
    res.status(500).json({
      error: 'Error fetching statement'
    })
  }
})

// Create uploads directory if it doesn't exist
import fs from 'fs'
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads')
}

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`)
}) 