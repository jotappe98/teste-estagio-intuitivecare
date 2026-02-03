<template>
  <div class="operadoras">
    <h2>Lista de Operadoras</h2>

    <table v-if="operadoras">
      <thead>
        <tr>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>UF</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="op in operadoras.data" :key="op.CNPJ">
          <td>{{ op.CNPJ }}</td>
          <td>{{ op.RAZAO_SOCIAL }}</td>
          <td>{{ op.UF }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Paginação -->
    <div v-if="operadoras" class="paginacao">
      <!-- seta esquerda -->
      <button @click="paginaAnterior" :disabled="page === 1">
        ◀
      </button>

      <!-- números das páginas -->
      <button
        v-for="p in paginasVisiveis"
        :key="p"
        @click="irParaPagina(p)"
        :class="{ ativa: p === page }"
      >
        {{ p }}
      </button>

      <!-- seta direita -->
      <button
        @click="proximaPagina"
        :disabled="page === totalPages"
      >
        ▶
      </button>
    </div>

    <p v-else>Carregando dados...</p>
  </div>
</template>

<script>
import { getOperadoras } from '../services/api.js'

export default {
  name: 'Operadoras',

  data() {
    return {
      operadoras: null,
      page: 1,
      limit: 10,
      totalPages: 0
    }
  },

  async mounted() {
    await this.carregarOperadoras()
  },

  computed: {
    paginasVisiveis() {
      const total = this.totalPages
      const atual = this.page
      const maxVisiveis = 6

      let inicio = Math.max(1, atual - 2)
      let fim = Math.min(total, inicio + maxVisiveis - 1)

      if (fim - inicio < maxVisiveis - 1) {
        inicio = Math.max(1, fim - maxVisiveis + 1)
      }

      const paginas = []
      for (let i = inicio; i <= fim; i++) {
        paginas.push(i)
      }

      return paginas
    }
  },

  methods: {
    async carregarOperadoras() {
      try {
        const response = await getOperadoras(this.page, this.limit)
        this.operadoras = response
        this.totalPages = Math.ceil(response.total / this.limit)
      } catch (error) {
        console.error('Erro ao carregar operadoras:', error)
      }
    },

    async proximaPagina() {
      if (this.page < this.totalPages) {
        this.page++
        await this.carregarOperadoras()
      }
    },

    async paginaAnterior() {
      if (this.page > 1) {
        this.page--
        await this.carregarOperadoras()
      }
    },

    async irParaPagina(pagina) {
      this.page = pagina
      await this.carregarOperadoras()
    }
  }
}
</script>

<style scoped>
.operadoras {
  margin-top: 20px;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin-top: 12px;
}

th,
td {
  border: 3px solid #000000;
  padding: 8px;
}

th {
  background-color: #e5e7eb;  /* cinza claro */
  color: #111827;            /* texto escuro */
  text-align: left;
}

.paginacao {
  margin-top: 16px;
  display: flex;
  gap: 6px;
  align-items: center;
}

.paginacao button {
  padding: 6px 10px;
  border: 1px solid #d1d5db;
  background: #f3f4f6;      /* cinza claro */
  color: #111827;          /* texto escuro */
  cursor: pointer;
  border-radius: 4px;
}

.paginacao button:hover {
  background: #e5e7eb;
}


.paginacao button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.paginacao button.ativa {
  background: #2563eb;
  color: white;
  font-weight: bold;
}

tbody tr:nth-child(even) {
  background-color: #f9fafb; /* cinza bem claro */
}

tbody tr:nth-child(odd) {
  background-color: #ffffff;
}

td {
  color: #111827;
}


</style>
