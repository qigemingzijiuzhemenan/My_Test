#此模块是请求详细操作

import requests
import json
class Requests():
    headers = {"Authorization": "",
               "Content-Type":"application/json"}

    def __init__(self):
        self.url = "http://dev.api.jfvz.ssoct.cn/"
        # self.url = "http://dj.ssoct.cn/"
    def get_requests(self,api):
        headers = {}
        try:
            url = self.url + api
            res = requests.get(url=url, headers=Requests.headers)  # verify=False做https请求用的
            response = res.json()
            # print(response)
            # print("请求状态：", res.status_code)
            # for key in response:
            #     print(str(key), ":", str(response[key]))
            code = res.status_code
            return code, response,url
        except Exception as Error:
            print("请求出错，原因是：%s" % (Error))
        # if api == "api/Members/UserInfo":
        #     self.memberId = response["Id"]
        # elif api == "api/Members/{}":
        #     self.organizationId = response["Organization"]["Id"]
        # print('\n')


    def post_requests(self,api,data):
        try:
            url = self.url + api
            res = requests.post(url=url, headers=Requests.headers, data=data)  # verify=False做https请求用的
            response = res.json()  # verify=False做https请求用的
            # print(response)
            # print("请求状态：", res.status_code)
            # for key in response:
            #     print(str(key), ":", str(response[key]))
            if api == "token":
                Requests.headers["Authorization"] = "bearer" + " " + response["access_token"]
            code = res.status_code
            return code, response,url
        except Exception as Error:
            print("请求出错，原因是：%s" % (Error))

        print('\n')


#测试此模块
# test = Requests()
# api = "api/Members/47cadf47-31e9-4e08-a312-28b3f6965dbe"
# data = None
# headers = {}
# method = "get"
# test  = test.get_requests(api,headers)
# print(test)



# api_1 = "api/Members/UserInfo"
#
# headers_1 = {"Content-Type":"application/x-www-form-urlencoded"}
# test.get_requests(api_1,headers_1)