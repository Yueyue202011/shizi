import pymysql

# def chaxun(sql):
#     """
#         查询 可视化 数据库
#     """
#     # pymysql 连接数据库
#     db = pymysql.connect(host="192.168.1.110",user="root",password="root",db="dsm")

#     # 获取游标：查询窗口
#     cur = db.cursor()

#     # 执行sql语句
#     cur.execute(sql)

#     # 得到执行的结果
#     res = cur.fetchall()

#     # 关闭程序
#     db.close()

#     return res
# sql = "select * from 长安_Sheet1_csv a join 长安_Sheet2_csv b on a.a = b.a join 长安_Sheet3_csv c on a.a = c.a"
# a = chaxun(sql)
# print(a)






def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="192.168.1.110",user="root",password="root",db="dsm")

    # 获取游标：查询窗口
    cur = db.cursor()

    # 执行sql语句
    cur.execute(sql)

    # 提交修改
    db.commit()

    # 关闭程序
    db.close()

    return True

sql = 'INSERT INTO 长安_sheet1_csv (a,b) VALUES (999,"柿子")'
b = commit(sql)
print(b)