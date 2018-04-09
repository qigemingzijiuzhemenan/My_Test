#此模块是对接口请求过程的封装

from  Interface.request import Requests
resqus = Requests()
class Api_Test():
    def __init__(self,api,method,data):
        self.api = api
        self.method = method
        if data:
            self.data=eval(data)
        else:
            self.data = data
    def apitest(self):
        if self.method =="get":
            r = resqus.get_requests(self.api)
        elif self.method =="post":
            r = resqus.post_requests(self.api,self.data)
        return r
    # 获取请求状态码
    def get_status(self):
        return self.apitest()[0]

    # 获取请求内容
    def get_conten(self):
        return self.apitest()[1]

    def get_url(self):
        return self.apitest()[2]

    # #获取请求信息类型
    # def get_content_type(self):
    #     rp_headers = self.apitest().headers
    #     return rp_headers


# 测试此模块
# api = "api/Members/47cadf47-31e9-4e08-a312-28b3f6965dbe"
# data = None
# headers = None
# method = "get"
# test = Api_Test(api,method,headers,data)
# print(test.get_status())
# print(test.get_conten())