import cx_Oracle

class DB():
    #连接数据库
    def __init__(self):
        #Oracle的参数
        self.username = ""
        self.password = ""
        self.host = ""
        self.port = "1521"
        self.sid = ""
        self.dsn = cx_Oracle.makedsn(self.host,self.port,self.sid)

    # 创建连接对象
    def __connect_databases(self):
        try:
            # 创建连接
            self.conn = cx_Oracle.connect(self.username,self.password,self.dsn)
            cursor = self.conn.cursor()  # 创建游标
            return cursor
        except cx_Oracle.Error as Error:
            print("数据库连接失败：%s" % (Error))

        #查询数据
    def select_data(self,SQL):
        try:
            cursor = self.__connect_databases()     #建立游标
            cursor.execute(SQL)      #在游标上使用SQL语句
            name = cursor.description
            values = cursor.fetchall()    #返回所有数据
            # row = cursor.fetchone()  #返回一行数据
            # row = cursor.fetchmany(2)#返回两行数据
            data = []
            num = 0
            while num < len(values):
                # print(values[num])
                # d = []
                num_1 = 0
                c = {}
                while num_1 < len(name):
                    c[name[num_1][0]] = values[num][num_1]
                    num_1 += 1
                data.append(c)
                # print(d)
                num += 1
            return data
        except cx_Oracle.Error as Error:
            print("查询出错：%s" % (Error))
        finally:  # 无论怎样都会执行下面的关闭连接数据库的代码
            self.conn.close()


#测试此模块

db = DB()
sql = 'select * from T_ZJLD_BSXLB'

data = db.select_data(sql)
for b in data:
    print(b)
