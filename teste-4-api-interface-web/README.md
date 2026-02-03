# Teste 4 — API e Interface Web

Este teste consiste na criação de uma API em Python (Flask) e uma interface web em Vue.js para visualização de dados de operadoras de planos de saúde e suas despesas.

O objetivo foi disponibilizar endpoints simples para consulta dos dados e um frontend básico para listagem e navegação com paginação.

---

## Tecnologias utilizadas

- Backend: Python 3 + Flask  
- Frontend: Vue 3 + Vite  
- Consumo de dados via CSV (gerados nos testes anteriores)  

---

COMO EXECUTAR O BACK-END:

1. Acesse a pasta do backend:
```bash
cd teste-4-api-interface-web/backend

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
venv\Scripts\activate   # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Inicie a API:

python app.py

A API ficará disponível em:

http://localhost:5000

Rotas disponíveis

GET /api/operadoras?page=1&limit=10
Lista operadoras com paginação.

GET /api/operadoras/{cnpj}
Retorna os dados de uma operadora específica.

GET /api/operadoras/{cnpj}/despesas
Retorna o histórico de despesas da operadora.

GET /api/estatisticas
Retorna estatísticas agregadas (total, média e top 5 operadoras).

---

COMO EXECUTAR O FRONT-END:

1.Acesse a pasta do frontend:

cd teste-4-api-interface-web/frontend


2.Instale as dependências:

npm install


3.Inicie o servidor de desenvolvimento:

npm run dev


O frontend ficará disponível em:

http://localhost:5173

Funcionalidades implementadas:

Listagem de operadoras em tabela
Paginação no frontend consumindo paginação da API
Navegação por páginas com botões numéricos
Integração entre frontend e backend
Tratamento básico de loading e erros de requisição

Decisões técnicas (trade-offs)

Framework backend (Flask):

Escolhi Flask por ser simples, leve e suficiente para o escopo do teste e também por ter mais familiriade com a ferramenta.

Paginação (offset-based):
Utilizei paginação por página/limite por ser simples de implementar e adequada para o volume de dados esperado.

Busca/filtro no servidor:
A busca foi pensada para ser feita no backend para evitar carregar muitos dados no frontend.

Gerenciamento de estado no frontend:
Foi utilizado apenas estado local no componente (data, methods e computed), pois a aplicação é simples e não há necessidade de uma store global.

Tratamento de erros e loading:
Erros de requisição são capturados no frontend e o usuário visualiza estados de carregamento enquanto os dados são buscados.

