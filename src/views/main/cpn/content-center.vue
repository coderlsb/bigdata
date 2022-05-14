<template>
  <div class="content-center">
    <map-echart :map-data="data1" bkcolor="#0a0e42" ref="mapp"></map-echart>
    <div class="tongji">
      <dv-border-box-11 title="滚动数据">
        <div class="gundong">
          <dv-border-box-8>
            <dv-scroll-board
              :config="config"
              style="width: 600px; height: 300px"
            />
          </dv-border-box-8>
        </div>
      </dv-border-box-11>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, reactive, computed } from 'vue'
import { mapEchart, basiczhuEchart } from '@/components/page-echarts'
import LocalCache from '@/utils/cache'
import baseEchart from '@/base-ui/echart'
import { useStore } from 'vuex'

export default defineComponent({
  components: {
    mapEchart
  },
  setup() {
    const store = useStore()
    let hours: any[] = reactive([])
    let minutes: any[] = reactive([])
    let seconds: any[] = reactive([])
    const data = LocalCache.getCache('name').name
    const data1 = data.map((item: any) => {
      return { name: item.cityName, value: item.dayHeighestTem }
    })

    const lastdata = store.state.lastdata

    const config = {
      header: ['城市', '天气', '风向', '等级', '最高温度'],
      headerBGC: '#11359d',
      evenRowBGC: '# 0b0f43',
      oddRowBGC: '# 0b0f43',
      data: lastdata,
      columnWidth: [200, 200, 200, 200, 200],

      align: ['center'],
      carousel: 'page'
    }
    const data2 = computed(() => {
      const XData: string[] = []
      const YData: string[] = []
      const LowTem = store.state.lowTem
      for (const item of LowTem) {
        XData.push(item.cityName)
        YData.push(item.nitLowestTem)
      }
      return { XData, YData }
    })
    return {
      data1,
      data2,
      config
    }
  }
})
</script>

<style scoped>
.content-center {
  flex: 1 1 auto;
}

.tongji {
  width: 100%;
  height: 420px;
  position: relative;
}
.gundong {
  position: absolute;
  left: 120px;
  bottom: 32px;
}
</style>
