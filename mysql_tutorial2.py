# ! /usr/bin/python
# -*- coding: utf-8 -*-

sql = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (18684928,18684928,"内蒙古赤峰市巴林左旗","联通林东镇新城区BRAS数据机房")'
sql_tmp = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (%s, %s, %s, %s)'
values = [(16890112,16891391,"泰国","曼谷"),(16891392,16891647,"泰国","如果硅农"), (16891648,16892159,"泰国","加拉信府")]


# mysql-connector
print('mysql-connector'.center(50, '='))
from mysql import connector

cnx = connector.Connect(host="pythontest.cgngr7chq0yp.ap-northeast-1.rds.amazonaws.com", user="jilu",
                            password="123456", database="pythontest", charset="utf8")
cnx.autocommit = True
db0 = cnx.cursor()
print db0.execute(sql)
print db0.executemany(sql_tmp, values)

# MySQLdb
print('MySQLdb'.center(50, '='))
import MySQLdb

def connect_mysql(db_host="pythontest.cgngr7chq0yp.ap-northeast-1.rds.amazonaws.com", user="jilu",
                   passwd="123456",db="pythontest", charset="utf8"):
    conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
    conn.autocommit(True)
    return conn.cursor()
db1 = connect_mysql()
print db1.execute(sql), db1.lastrowid
print db1.executemany(sql_tmp, values), db1.lastrowid


# torndb
print('torndb1'.center(50, '='))
import torndb

db2 = torndb.Connection(
    host='pythontest.cgngr7chq0yp.ap-northeast-1.rds.amazonaws.com',
    database='pythontest',
    user='jilu',
    password='123456',
    charset="utf8")
print db2.insert(sql)
print db2.insertmany(sql_tmp, values)