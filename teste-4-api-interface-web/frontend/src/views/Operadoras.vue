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

    <p v-else>Carregando dados...</p>
  </div>
</template>

<script>
import { getOperadoras } from '../services/api.js'

export default {
  name: 'Operadoras',

  data() {
    return {
      operadoras: null
    }
  },

  async mounted() {
    try {
      this.operadoras = await getOperadoras()
    } catch (error) {
      console.error(error)
    }
  }
}
</script>

<style>
.operadoras {
  margin-top: 20px;
}
</style>
