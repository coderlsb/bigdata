export interface Data {
  provinceNAme: string
  cityName: string
  whiteDay: string
  dayWeCondition: string
  dayFlowDirect: string
  dayFlowGrade: string
  dayHeighestTem: string
  blackDay: string
  nitWeCondition: string
  nitFlowDirect: string
  nitFlowGrade: string
  nitLowestTem: string
}
export interface IData {
  name: Array<Data>
}
export interface Data1 {
  cityName: string
  dayHeighestTem: string
}
export interface IData1 {
  name: Array<Data1>
}
