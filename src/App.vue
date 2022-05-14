<template>
  <div class="app">
    <main-vue></main-vue>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import mainVue from './views/main/main.vue'
export default defineComponent({
  name: 'App',
  components: {
    mainVue
  }
})
</script>

<style lang="less">
.app {
  width: 100%;
  height: 100%;
}
</style>
