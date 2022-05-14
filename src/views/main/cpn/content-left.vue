<template>
  <div class="content-left">
    <div class="yoyo">
      <div class="title">全国气温情况流动图</div>
      <zhu-echart :XData="XData1" :YData="YData1"></zhu-echart>
    </div>
    <div class="yoyo1">
      <div class="title">天气情况</div>
      <pie-echart :pieData="type"></pie-echart>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed, reactive } from 'vue'
import { zhuEchart, pieEchart } from '@/components/page-echarts'
import LocalCache from '@/utils/cache'
import { useStore } from 'vuex'

export default defineComponent({
  components: {
    zhuEchart,
    pieEchart
  },
  setup() {
    //盾冬
    const store = useStore()
    const XData: string[] = []
    const YData: string[] = []
    const XData1: string[] = reactive([])
    const YData1: string[] = reactive([])
    const data = LocalCache.getCache('name').name
    for (const item of data) {
      XData.push(item.cityName)
      YData.push(item.dayHeighestTem)
    }
    for (let i = 0; i < 5; i++) {
      XData1.push(XData[i])
      YData1.push(YData[i])
    }
    setInterval(function () {
      XData1.shift()
      const numb = Math.round(Math.random() * (456 + 1))
      XData1.push(XData[numb])
      YData1.shift()
      YData1.push(YData[numb])
    }, 2100)
    //type
    const data2 = store.state.type
    const type = computed(() => {
      return data2.map((item: any) => {
        return { name: item.weType, value: item.number }
      })
    })
    return {
      XData1,
      YData1,
      type
    }
  }
})
</script>

<style scoped>
.content-left {
  flex: 0 0 500px;
  width: 100%;
  height: 100%;
  margin-left: 30px;
}
.yoyo {
  width: 100%;
  height: 420px;
  background-image: url('../../../assets/img/panel-l-b.png');
}
.yoyo1 {
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
