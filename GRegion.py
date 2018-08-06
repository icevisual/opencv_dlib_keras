import pymysql
import sys
from collections import OrderedDict

if __name__ == '__main__':
  conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='',db='admin',charset='utf8')
  cursor = conn.cursor()
  sql = """SELECT
  cid,
  cup,
  type,
  `name`
FROM
  adm_area
WHERE
  type > 0
AND type < 3
ORDER BY type ASC,cid ASC"""
  cursor.execute(sql)
  print("cursor.excute:",cursor.rowcount)
  XMLDict = OrderedDict()
  datas = cursor.fetchall()
  for line in datas:
    if line[2] == 1:
      XMLDict[line[0]] = {
        "Name" : line[3],
        "Child" : []
      }
    if line[2] == 2:
      XMLDict[line[1]]["Child"].append({
        "Name" : line[3]
      })
  result_str = "";
  for province in XMLDict:
    child_str = "";
    for city in XMLDict[province]["Child"]:
      child_str = "%s<City Name='%s'/>" % (child_str,city["Name"]) 
    if len(XMLDict[province]["Child"]) == 0:
      result_str = "%s<Province Name='%s'><City Name='%s'/></Province>" % (result_str, XMLDict[province]["Name"], XMLDict[province]["Name"]) 
    else:
      result_str = "%s<Province Name='%s'>%s</Province>" % (result_str, XMLDict[province]["Name"],child_str) 
  f = open("res.txt", 'w')
  f.write(result_str)
  f.close()


