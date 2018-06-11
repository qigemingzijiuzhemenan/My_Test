import cx_Oracle

class DB():
    #连接数据库
    def __init__(self):
        #Oracle的参数
        self.username = "szjpt"
        self.password = "Azljd540!"
        self.host = "192.168.59.24"
        self.port = "1521"
        self.sid = "orcl"
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

        #查询第一行数据
    def select_data(self,SQL):
        try:
            cursor = self.__connect_databases()     #建立游标
            cursor.execute(SQL)      #在游标上使用SQL语句
            name = cursor.description
            # row = cursor.fetchone()  #返回一行数据
            # row = cursor.fetchmany(2)#返回两行数据
            row = cursor.fetchall()    #返回所有数据
            return name,row
        except cx_Oracle.Error as Error:
            print("查询出错：%s" % (Error))
        finally:                          #无论怎样都会执行下面的关闭连接数据库的代码
            self.conn.close()


#测试此模块

db = DB()
sql = 'select * from T_ZJLD_BSXLB'

keys,values = db.select_data(sql)
# print(values)
# print(keys)
data = {}
for i in range(len(keys)):
    data[keys[i][0]] = []
    for a in range(len(values)):
        data[keys[i][0]].append(values[a][i])

for b in data.items():
    print(b)