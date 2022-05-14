<template>
  <div class="zhu-echart">
    <base-echart :options="options" width="500px"></base-echart>
  </div>
</template>

<script setup lang="ts">
import { defineProps, computed, ref, onMounted } from 'vue'
import BaseEchart from '@/base-ui/echart'
import { IDataType } from '../types/index'
import { color } from 'echarts'
const props = defineProps<{
  XData: string[]
  YData: string[]
  title?: string
}>()

const options = computed(() => {
  return {
    // title: {
    //   text: props.title,
    //   textStyle: {
    //     color: 'yellowgreen',
    //     fontSize: 13
    //   }
    // },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: '#283b56'
        }
      }
    },

    toolbox: {
      show: true
    },
    dataZoom: {
      show: false,
      start: 0,
      end: 100
    },
    xAxis: [
      {
        type: 'category',
        boundaryGap: true,
        data: props.XData
      },
      {
        type: 'category',
        boundaryGap: true,
        data: props.YData
      }
    ],

    yAxis: [
      {
        type: 'value',
        scale: true,
        name: 'temperoy',
        max: 40,
        min: 0,
        boundaryGap: [0.2, 0.2]
      }
    ],
    series: [
      {
        name: 'Dynamic Bar',
        type: 'bar',
        // xAxisIndex: 1,
        // yAxisIndex: 1,
        data: props.YData
      }
    ]
  }
})
</script>

<style lang="scss" scoped></style>
