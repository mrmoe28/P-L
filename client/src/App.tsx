import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import HomePage from './components/layout/HomePage'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <HomePage />
    </QueryClientProvider>
  )
}

export default App
