# 将生成的优惠券存入Mysql中
# 2018年03月14日18:13:34
import pymysql
import random
import string

db = pymysql.connect("localhost", "root", "maxwell", "cupon")
cursor = db.cursor()
cursor.execute("drop table if exists cuponlist")
sql = "create table cuponlist(id int auto_increment, cupon char(40), primary key (id))"
cursor.execute(sql)

candidate = string.ascii_letters
ans, times = dict(), 0
while times < 200:
    res = ''
    for i in range(20):
      res += random.choice(candidate)
    if res not in ans:
        ans[res] = 1
        times += 1
        # sql = "insert into cuponlist(cupon) values (\'%s\')" % res
        # cursor.execute(sql)
        cursor.execute("insert into cuponlist(cupon) values (%s)", res)
db.commit()
db.close()
