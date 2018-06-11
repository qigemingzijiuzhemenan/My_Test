# encoding: utf-8
import pymysql
class DB():
    #连接数据库
    def __init__(self):
        #MySQL的参数
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root_1"
        self.password = "123456"
        self.database = "dangjian"

    # 创建连接对象
    def __connect_databases(self):
        try:
            # 创建连接
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        port=self.port,
                                        password=self.password,
                                        database=self.database,
                                        charset='utf8')
            cursor = self.conn.cursor()  # 创建游标
            return cursor
        except pymysql.Error as Error:
            print("数据库连接失败：%s" % (Error))

        #查询第一行数据
    def select_data(self,SQL):
        try:
            cursor = self.__connect_databases()     #建立游标
            cursor.execute(SQL)      #在游标上使用SQL语句
            name = cursor.description
            values = cursor.fetchall()  # 返回所有数据
            # row = cursor.fetchone()  #返回一行数据
            # row = cursor.fetchmany(2)#返回两行数据
            data = {}
            for i in range(len(name)):
                data[name[i][0]] = []
                for a in range(len(values)):
                    data[name[i][0]].append(values[a][i])
            return data
        except pymysql.Error as Error:
            print("查询出错：%s" % (Error))
        finally:  # 无论怎样都会执行下面的关闭连接数据库的代码
            self.conn.close()


#测试此模块

# db = DB()
# sql = 'select * from activity;'
#
# data = db.select_data(sql)
# # print(values)
# # print(keys)
# for b in data.items():
#     print(b)
