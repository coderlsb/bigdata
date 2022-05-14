import lsRequest from '..'
import { IData, IData1 } from './type'

export function requestData(): any {
  return lsRequest.request<IData1>({
    url: 'datatr/'
  })
}

export function requestData1(): any {
  return lsRequest.request<IData1>({
    url: 'estdata/'
  })
}
export function requestData2(): any {
  return lsRequest.request<IData1>({
    url: 'wetype/'
  })
}
export function requestData3(): any {
  return lsRequest.request<IData1>({
    url: 'lowtem/'
  })
}
export function requestData4(): any {
  return lsRequest.request<IData1>({
    url: 'feng/'
  })
}
export function requestData5(): any {
  return lsRequest.request<IData1>({
    url: 'lastdata/'
  })
}
