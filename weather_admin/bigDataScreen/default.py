import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',password="lsbqwe",database="weatherdb")
cur = db.cursor()

def GetWeather():
    sql = '''select cityName,dayHeighestTem from weather
             '''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        # data.append({"provinceNAme":i[0],"cityName":i[1],"whiteDay":i[2],"dayWeCondition":i[3],"dayFlowDirect":i[4],
        #              "dayFlowGrade":i[5],"dayHeighestTem":i[6],"blackDay":i[7],
        #              "nitWeCondition":i[8],"nitFlowDirect":i[9],"nitFlowGrade":i[10],"nitLowestTem":i[11]})
        data.append({"cityName":i[0],"dayHeighestTem":i[1]})

    return data
def GetHighestTem():
    sql ='''select cityName,dayHeighestTem from weather
            order by dayHeighestTem desc limit 11'''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        data.append({"cityName": i[0], "dayHeighestTem": i[1]})
    return data

def GetType():
    sql = ''' select dayWeCondition,count(dayWeCondition) from weather
              group by dayWeCondition
              order by count(dayWeCondition)'''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        data.append({"weType": i[0], "number": i[1]})
    return data
def GetLowTem():
    sql ='''select cityName,nitLowestTem from weather
            order by nitLowestTem desc limit 10'''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        data.append({"cityName": i[0], "nitLowestTem": i[1]})
    return data
def window():
    sql = ''' select dayFlowDirect,count(dayFlowDirect) from weather
                  group by dayFlowDirect
                  order by count(dayFlowDirect)'''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        data.append({"cityName": i[0], "dayFlowDirect": i[1]})
    return data
def lastData():
    sql = ''' select cityName,dayWeCondition,dayFlowDirect,dayFlowGrade,dayHeighestTem  from weather
                     '''
    cur.execute(sql)
    data = []
    for i in cur.fetchall():
        data.append({"cityName": i[0], "dayWeCondition": i[1],"dayFlowDirect":i[2],"dayFlowGrade":i[3],"dayHeighestTem":i[4]})
    return data
