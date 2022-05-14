import { createStore, Store, useStore as useVuexStore } from 'vuex'
import { IState } from './types'
import {
  requestData,
  requestData1,
  requestData2,
  requestData3,
  requestData4,
  requestData5
} from '@/service/shuju/shuju'
import LocalCache from '@/utils/cache'
const store = createStore<IState>({
  state: () => {
    return {
      name: [],
      range: [],
      type: [],
      feng: [],
      lowTem: [],
      lastdata: []
    }
  },
  mutations: {
    changeName(state, name: []) {
      state.name = name
    },
    chageLastData(state, lastdata: []) {
      state.lastdata = lastdata
    },
    changeFeng(state, feng: []) {
      state.feng = feng
    },
    changeLowTem(state, lowTem: []) {
      state.lowTem = lowTem
    },
    changeRange(state, range: []) {
      state.range = range
    },

    changeType(state, type: []) {
      state.type = type
    }
  },
  actions: {
    async LoaDingData(state) {
      const result = await requestData()
      state.commit('changeName', result.name)
      LocalCache.setCache('name', result)
      // 最高温度
      const result2 = await requestData1()
      state.commit('changeRange', result2.range)
      LocalCache.setCache('range', result2.range)
      //type
      const result3 = await requestData2()

      state.commit('changeType', result3.WeType)
      LocalCache.setCache('type', result3.WeType)

      const result4 = await requestData3()
      state.commit('changeLowTem', result4.LowTem)
      LocalCache.setCache('LowTem', result4.LowTem)

      const result5 = await requestData4()
      state.commit('changeFeng', result5.feng)
      LocalCache.setCache('feng', result5.feng)

      const result6 = await requestData5()
      state.commit('chageLastData', result6.lastdata)
      LocalCache.setCache('lastdata', result6.lastdata)
    },
    loadLocalLogin({ commit }) {
      const lastdata = LocalCache.getCache('lastdata')
      if (lastdata) {
        commit('chageLastData', lastdata)
      }
      const name = LocalCache.getCache('name')
      if (name) {
        commit('changeName', name)
      }
      const range = LocalCache.getCache('range')
      if (range) {
        commit('changeRange', range)
      }
      const type = LocalCache.getCache('type')
      if (type) {
        commit('changeType', type)
      }
      const feng = LocalCache.getCache('feng')
      if (feng) {
        commit('changeFeng', feng)
      }
      const LowTem = LocalCache.getCache('LowTem')
      if (LowTem) {
        commit('changeLowTem', LowTem)
      }
    }
  }
})
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export function setupStore() {
  store.dispatch('LoaDingData')
  store.dispatch('loadLocalLogin')
}

export function useStore(): Store<IState> {
  return useVuexStore()
}

export default store
