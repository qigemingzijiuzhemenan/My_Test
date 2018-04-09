from Case.Get_excel import read_casefile
from Interface.request_fengzhuang import Api_Test
cases = read_casefile()
class Run_case():
    def testinterface(self):
        test_pass = 0
        test_fail = 0
        test_json = []
        test_url = []
        test_data = []
        test_method = []
        test_hope = []
        test_relust = []
        test_number = []
        test_name = []
        for i in range(len(cases)):
            test = Api_Test(cases[i]["api"],cases[i]["method"],cases[i]["data"])
            api_number = cases[i]["api_number"]
            api_name = cases[i]["api_name"]
            api_url = test.get_url()
            api_hope = cases[i]["hope"]
            api_data = cases[i]["data"]
            api_method = cases[i]["method"]
            api_code = test.get_status()
            api_content = test.get_conten()

            test_number.append(api_number)
            test_name.append(api_name)
            test_url.append(api_url)
            test_data.append(api_data)
            test_method.append(api_method)
            test_hope.append(api_hope)
            test_json.append(api_content)
            api_hope = eval(api_hope)
            if api_content == api_hope:
                test_pass+=1
                test_relust.append("pass")
            elif api_code ==500:
                test_fail += 1
                test_relust.append("fail")
            else:
                test_fail+=1
                test_relust.append("fail")
        print("通过%d个测试"%test_pass)
        print("不通过%d个测试"%test_fail)
        return test_number,\
               test_name,\
               test_url,\
               test_data,\
               test_method,\
               test_hope,\
               test_json,\
               test_relust,\
               test_pass,\
               test_fail





# 测试此模块
# test = Run_case()
# test.testinterface()