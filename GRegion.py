import pymysql

 
def trans_dict_to_xml(data):
  """
  将 dict 对象转换成微信支付交互所需的 XML 格式数据
 
  :param data: dict 对象
  :return: xml 格式数据
  """
 
  xml = []
  for k in sorted(data.keys()):
    v = data.get(k)
    if k == 'detail' and not v.startswith('<![CDATA['):
      v = '<![CDATA[{}]]>'.format(v)
    xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
  return '<xml>{}</xml>'.format(''.join(xml))

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
ORDER BY type ASC"""
  cursor.execute(sql)
  print("cursor.excute:",cursor.rowcount)
  XMLDict = {

  }
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
    result_str = "%s<Province Name='%s'>%s</Province>" % (result_str, XMLDict[province]["Name"],child_str) 
    print(result_str)
  f = open("res.txt", 'w')
  f.write(result_str)
  f.close()


