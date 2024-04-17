<template>
  <MiniProfileBlock />
</template>

<script>
import MiniProfileBlock from './components/MiniProfileBlock.vue'

export default {
  name: 'App',
  components: {
    MiniProfileBlock
  }
}
</script>

<style>
#block_mini_profile {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
