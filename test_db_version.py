#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# connect database
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="mini")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# execute SQL order
cursor.execute("SELECT VERSION()")

# fetchone() to get one data
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect database
db.close()

