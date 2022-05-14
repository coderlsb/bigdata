import axios from 'axios'
import type { AxiosInstance, AxiosRequestConfig } from 'axios'
class LSRequest {
  instance: AxiosInstance
  constructor(config: AxiosRequestConfig) {
    this.instance = axios.create(config)
    this.instance.interceptors.response.use((res) => {
      return res.data
    })
  }
  request<T>(config: AxiosRequestConfig<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.instance.request<any, T>(config).then((res) => {
        resolve(res)
      })
    })
  }
}

export default LSRequest
