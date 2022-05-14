<template>
  <div class="header">
    <h1 class="header-title">大数据可视化平台</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    return {}
  }
})
</script>

<style scoped>
.header {
  height: 28px;
  width: 100%;
}
.header .header-title {
  line-height: 64px;
  text-align: center;
  font-size: 35px;
  font-weight: 400;
  color: yellowgreen;
  margin: 0 auto;
}
</style>
