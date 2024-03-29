import unittest
from HTMLTestRunner import HTMLTestRunner
from test.test_login import Test_login
from test.sys_user_add import Test_add_sys_user
from  test.student_page import Test_student_page
from test.activity_page import Test_activity_page
# from config.config import logger
import os
import sys
report_path = os.path.join(os.getcwd(),'test_report')
print(report_path)
import time

def suite():



    test_login = unittest.makeSuite(Test_login,'test')
    test_add_sys_user = unittest.makeSuite(Test_add_sys_user,'test')
    test_student_page = unittest.makeSuite(Test_student_page,'test')
    test_activity_page = unittest.makeSuite(Test_activity_page,'test')
    Test = unittest.TestSuite([test_login,test_student_page,test_activity_page])

    return Test

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M')



    filename = os.path.join(report_path,'api_test' + now + '.html')



    fp = open(filename, 'wb+')


    runner = HTMLTestRunner(stream=fp,title = '接口测试',description='描述')
    runner.run(suite())