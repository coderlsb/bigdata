<template>
  <div class="main">
    <header-vue></header-vue>
    <content-vue></content-vue>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import headerVue from './cpn/header.vue'
import contentVue from './cpn/content.vue'
export default defineComponent({
  components: {
    headerVue,
    contentVue
  },
  setup() {
    return {}
  }
})
</script>

<style scoped>
.main {
  width: 100%;
  height: 100%;
}
</style>
