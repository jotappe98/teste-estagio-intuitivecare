<template>
  <div class="app">
    <h1>Teste 4 — Interface Web</h1>

    <Operadoras />
  </div>
</template>

<script>
import Operadoras from './views/Operadoras.vue'

export default {
  name: 'App',
  components: {
    Operadoras
  }
}
</script>

<style>
.app {
  padding: 20px;
  font-family: Arial, sans-serif;
}
</style>
