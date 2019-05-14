# encoding = utf-8
from selenium import webdriver
import time
import unittest
from table.Table import Table


class TestTableOpertion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    def testTable(self):
        url = "file:///Users/doudou/Desktop/table.html"
        self.driver.get(url)

        webTable = self.driver.find_elements_by_tag_name("table")
        table = Table(webTable)
        print(table.getRowCount())
        print(table.getColumnCount())
        # 获取表格第二行第三列单元格对象
        cell = table.getCell(2,3)
        # 断言获取的单元格文本内容是否是"第二行第三列"
        self.assertAlmostEqual("第二行第三列", cell.text)
        # 获取表格中第三行第二列单元格中的输入框对象
        cellInput = table.getWebElementInCell(3,2,"tag name","input")
        # 在找到的输入框中输入"第三行的第二列表格被找到"关键字内容
        cellInput.send_keys("第三行的第二列表格被找到")
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()