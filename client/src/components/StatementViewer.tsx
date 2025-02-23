import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

interface StatementViewerProps {
  statementId: string | null
}

interface Transaction {
  id: string
  date: string
  description: string
  amount: number
  category: string
  type: 'income' | 'expense'
}

interface StatementData {
  totalIncome: number
  totalExpenses: number
  transactions: Transaction[]
}

const StatementViewer = ({ statementId }: StatementViewerProps) => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['statement', statementId],
    queryFn: async () => {
      if (!statementId) return null
      const response = await axios.get(`http://localhost:3000/api/statements/${statementId}`)
      return response.data as StatementData
    },
    enabled: !!statementId,
  })

  if (!statementId) {
    return (
      <div className="text-gray-500 text-center py-8">
        Upload a statement to view the analysis
      </div>
    )
  }

  if (isLoading) {
    return (
      <div className="text-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        <p className="mt-2 text-gray-600">Analyzing statement...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-red-600 text-center py-8">
        Error loading statement analysis
      </div>
    )
  }

  if (!data) {
    return null
  }

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-2 gap-4">
        <div className="card bg-green-50">
          <h3 className="text-sm font-medium text-green-800">Total Income</h3>
          <p className="mt-2 text-2xl font-semibold text-green-900">
            ${data.totalIncome.toFixed(2)}
          </p>
        </div>
        <div className="card bg-red-50">
          <h3 className="text-sm font-medium text-red-800">Total Expenses</h3>
          <p className="mt-2 text-2xl font-semibold text-red-900">
            ${data.totalExpenses.toFixed(2)}
          </p>
        </div>
      </div>

      <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 rounded-lg">
        <table className="min-w-full divide-y divide-gray-300">
          <thead className="bg-gray-50">
            <tr>
              <th className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900">
                Date
              </th>
              <th className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                Description
              </th>
              <th className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                Category
              </th>
              <th className="px-3 py-3.5 text-right text-sm font-semibold text-gray-900">
                Amount
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200 bg-white">
            {data.transactions.map((transaction) => (
              <tr key={transaction.id}>
                <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900">
                  {new Date(transaction.date).toLocaleDateString()}
                </td>
                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {transaction.description}
                </td>
                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {transaction.category}
                </td>
                <td className={`whitespace-nowrap px-3 py-4 text-sm text-right ${
                  transaction.type === 'income' ? 'text-green-600' : 'text-red-600'
                }`}>
                  ${Math.abs(transaction.amount).toFixed(2)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default StatementViewer 