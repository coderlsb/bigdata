from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

# SQL 插入语句
sql = '''INSERT INTO weather
         (id, provinceName, cityName, whiteDay, dayWeCondition, dayFlowDirect, dayFlowGrade, dayHeighestTem, blackDay, nitWeCondition, nitFlowDirect, nitFlowGrade, nitLowestTem)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

# 数据库连接设置
db = pymysql.connect(host='localhost', user='root', password='lsbqwe', database='weatherDB')
cursor = db.cursor()

# 城市列表和键
allCity = []
key = 0

# 定义数据抓取函数
def scratchLs(tables, table_num):
    global key
    for i in range(table_num):
        trs = tables[i].findAll('tr')
        # 处理前两个tr
        tr1_td = trs[0].findAll('td')
        whiteDay = tr1_td[2].get_text().strip()
        blackDay = tr1_td[3].get_text().strip()
        tr2_td = trs[2].findAll('td')
        provinceName = tr2_td[0].get_text().strip()
        cityName = tr2_td[1].get_text().strip()
        # 白天数据
        dayWeCondition = tr2_td[2].get_text().strip()
        spans = tr2_td[3].findAll('span')
        dayFlowDirect = spans[0].get_text().strip()
        dayFlowGrade = spans[1].get_text().strip()
        dayHeighestTem = tr2_td[4].get_text().strip()
        # 夜间数据
        nitWeCondition = tr2_td[5].get_text().strip()
        spanss = tr2_td[6].findAll('span')
        nitFlowDirect = spanss[0].get_text().strip()
        nitFlowGrade = spanss[1].get_text().strip()
        nitLowestTem = tr2_td[7].get_text().strip()
        key += 1
        print(provinceName, cityName, whiteDay, dayWeCondition, dayFlowDirect, dayFlowGrade, dayHeighestTem, blackDay, nitWeCondition, nitFlowDirect, nitFlowGrade, nitLowestTem)
        cursor.execute(sql, (key, provinceName, cityName, whiteDay, dayWeCondition, dayFlowDirect, dayFlowGrade, dayHeighestTem, blackDay, nitWeCondition, nitFlowDirect, nitFlowGrade, nitLowestTem))
        db.commit()

        # 处理后续的tr
        for j in trs[3:]:
            tds = j.find_all('td')
            cityName = tds[0].get_text().strip()
            # 白天数据
            dayWeCondition = tds[1].get_text().strip()
            spans = tds[2].findAll('span')
            dayFlowDirect = spans[0].get_text().strip()
            dayFlowGrade = spans[1].get_text().strip()
            dayHeighestTem = tds[3].get_text().strip()
            # 夜间数据
            nitWeCondition = tds[4].get_text().strip()
            spanss = tds[5].findAll('span')
            nitFlowDirect = spanss[0].get_text().strip()
            nitFlowGrade = spanss[1].get_text().strip()
            nitLowestTem = tds[6].get_text().strip()
            key += 1
            print(provinceName, cityName, whiteDay, dayWeCondition, dayFlowDirect, dayFlowGrade, dayHeighestTem, blackDay, nitWeCondition, nitFlowDirect, nitFlowGrade, nitLowestTem)
            cursor.execute(sql, (key, provinceName, cityName, whiteDay, dayWeCondition, dayFlowDirect, dayFlowGrade, dayHeighestTem, blackDay, nitWeCondition, nitFlowDirect, nitFlowGrade, nitLowestTem))
            db.commit()

# 需要抓取的 URL 列表
urls = ['http://www.weather.com.cn/textFC/hb.shtml','http://www.weather.com.cn/textFC/db.shtml','http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml','http://www.weather.com.cn/textFC/hn.shtml','http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml']

for url in urls:
    html = urlopen(url)
    bsobj = BeautifulSoup(html.read(), features="lxml")
    tables = bsobj.findAll("table", {"width": "100%"})
    table_nums = len(bsobj.select('.lQCity > ul > li'))
    print(table_nums)
    scratchLs(tables, table_nums)

# 关闭数据库连接
db.close()
