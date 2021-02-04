# -*- coding: utf-8 -*-

import pymysql # 导入操作MySQL数据库的模块

userName="" # 记录用户名

# 打开数据库连接
def open():
    db = pymysql.connect(host="localhost", user="root", passwd="root", database="db_student",charset="utf8")
    return db # 返回连接对象

# 执行数据库的增、删、改操作
def exec(sql,values):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql,values) # 执行增删改的SQL语句
        db.commit() # 提交数据
        return 1 # 执行成功
    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败
    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接

# 带参数的精确查询
def query(sql,*keys):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql,keys) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果

# 不带参数的模糊查询
def query2(sql):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果
