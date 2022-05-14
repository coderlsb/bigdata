<template>
  <div class="content">
    <div class="wrapper">
      <content-left-vue></content-left-vue>
      <content-center-vue></content-center-vue>
      <content-right-vue></content-right-vue>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import contentLeftVue from './content-left.vue'
import contentCenterVue from './content-center.vue'
import contentRightVue from './content-right.vue'
export default defineComponent({
  components: {
    contentLeftVue,
    contentCenterVue,
    contentRightVue
  },
  setup() {
    return {}
  }
})
</script>

<style scoped>
.content {
  height: 100%;
  width: 100%;
  background: url('../../../assets/img/wrapper-bg.png') no-repeat;
  padding-top: 45px;
}
.wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: flex-start;
  align-items: stretch;
}
</style>
