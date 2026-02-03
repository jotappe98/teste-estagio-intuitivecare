const API_BASE_URL = 'http://localhost:5000'

export async function getOperadoras(page = 1, limit = 10) {
  const response = await fetch(
    `${API_BASE_URL}/api/operadoras?page=${page}&limit=${limit}`
  )

  if (!response.ok) {
    throw new Error('Erro ao buscar operadoras')
  }

  return response.json()
}

