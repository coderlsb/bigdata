<template>
  <div class="basiczhu-echart">
    <base-echart :options="options" width="761px" height="374px"></base-echart>
  </div>
</template>

<script setup lang="ts">
import { defineProps, computed, ref, onMounted } from 'vue'
import BaseEchart from '@/base-ui/echart'
import { IDataType } from '../types/index'

const props = defineProps<{
  XData: string[]
  YData: string[]
}>()

const options = computed(() => {
  return {
    xAxis: {
      type: 'category',
      data: props.XData
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: props.YData,
        type: 'bar'
      }
    ]
  }
})
</script>

<style lang="scss" scoped></style>
