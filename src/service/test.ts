import { IData } from './shuju/type'
import lsRequest from '.'

lsRequest
  .request<IData>({
    url: 'datatr/'
  })
  .then((res) => {
    console.log(res.name[3])
  })
