import LSRequest from './request'
import { BASE_URL, TIME_OUT } from './request/config'
const lsRequest = new LSRequest({
  baseURL: BASE_URL,
  timeout: TIME_OUT
})
export default lsRequest
