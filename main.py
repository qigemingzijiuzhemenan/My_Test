import datetime
from Case.Run_TestCase import Run_case
from report.Create_html import createHtml

if __name__=='__main__':
    starttime = datetime.datetime.now()
    testing = Run_case()
    test_number, test_name, test_url,test_data,test_method,test_hope,test_json, \
    test_relust,test_pass,test_fail = testing.testinterface()

    endtime = datetime.datetime.now()
    filename = './report/reprot.hrml'
    filepath = filename
    createHtml(filepath,starttime, endtime, test_number,test_name,test_url,test_data,
               test_method,test_hope,test_json,test_relust,test_pass,test_fail)
