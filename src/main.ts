import dataV from '@jiaminghi/data-view'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store'
import { setupStore } from './store'
import './assets/css/base.css'

// import '@/service/test'
const app = createApp(App)

import 'element-plus/dist/index.css'
setupStore()
app.use(dataV)
app.use(router)
app.use(store)
app.mount('#app')
