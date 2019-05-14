# encoding = utf-8
from selenium import webdriver
import unittest,time,os
from FileUtil import createDir
import traceback

picDir = createDir()

def takeScreenshot(driver,savepath,picname):
    picpath = os.path.join(savepath,str(picname)+ ".png")

    try:
        print(picname)
        driver.get_screenshot_as_file(picpath)
    except Exception as e:
        print(traceback.print_exc())


class TestFailCaptureScreen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSoGouSearch(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        try:
            self.driver.find_element_by_id("query").send_keys("光荣之路自动化测试")
            self.driver.find_element_by_id("stb").click()
            time.sleep(3)
            self.assertTrue("事在人为" in self.driver.page_source,"事在人为没有找到")
        except AssertionError as e:
            takeScreenshot(self.driver,picDir,e)
        except Exception as e:
            takeScreenshot(self.driver,picDir,e)
        except traceback as e:
            takeScreenshot(self.driver, picDir, e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()