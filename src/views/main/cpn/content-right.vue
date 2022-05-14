<template>
  <div class="content-right">
    <div class="okey">
      <div class="title">日间最高气温</div>
      <pie-echart :pie-data="rangeCount"></pie-echart>
    </div>
    <div class="okey1">
      <div class="title">日间风向分布</div>
      <pie-echart :pie-data="fengCount"></pie-echart>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import { pieEchart } from '@/components/page-echarts'
export default defineComponent({
  components: { pieEchart },
  setup() {
    const store = useStore()
    const range = store.state.range
    const feng = store.state.feng
    const rangeCount = computed(() => {
      return range.map((item: any) => {
        return { name: item.cityName, value: item.dayHeighestTem }
      })
    })
    const fengCount = computed(() => {
      return feng.map((item: any) => {
        return { name: item.cityName, value: item.dayFlowDirect }
      })
    })
    return { rangeCount, fengCount }
  }
})
</script>

<style scoped>
.content-right {
  flex: 0 0 500px;
  margin-right: 30px;
}
.okey {
  width: 100%;
  height: 420px;
  background-image: url('../../../assets/img/panel-l-b.png');
}
.okey1 {
  width: 100%;
  height: 420px;
  margin-top: 58px;
  background-image: url('../../../assets/img/panel-l-b.png');
}

.title {
  width: 100%;
  height: 44px;
  color: yellowgreen;
  line-height: 44px;
  text-align: center;
  background-image: url('../../../assets/img/title-bg.png');
}
</style>
