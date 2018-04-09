import xlrd
def read_casefile():
    filepach = ".\\Data\\casefile.xlsx"
    testcase = []
    casefile = xlrd.open_workbook(filepach)
    test_table = casefile.sheet_by_name("Sheet1")
    row_num = test_table.nrows  # 获取行数
    col_num = test_table.ncols  # 获取列数
    for i in range(row_num):
        if i != 0:
            case = {"api_number":test_table.row_values(i)[0],
                    "api_name":test_table.row_values(i)[1],
                    "api": test_table.row_values(i)[2],
                    "method": test_table.row_values(i)[3],
                    "headers": test_table.row_values(i)[4],
                    "data": test_table.row_values(i)[5],
                    "hope":test_table.row_values(i)[6]}
            testcase.append(case)
    return testcase


#测试此模块
# testcase = read_casefile()
# print(len(testcase))
