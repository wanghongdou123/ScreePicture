# encoding = utf-8
class Table(object):
    # 定义一个私有属性_table,用于存放table对象
    __table = ''


    def __init__(self,table):
        # table 类的构造方法
        self.setTable(table)

    def setTable(self, table):
        # 对私有属性进行赋值
        self.__table = table

    def getTable(self):
        # 获取私有属性__table的值
        return self.__table

    def getRowCount(self):
        # 回去table对象中的所有行的tr标签元素
        return len(self.__table.find_elements_by_tag_name("tr"))

    def getColumnCount(self):
        # 获取表格队形中的列数
        return  len(self.__table.find_elements_by_tag_name("tr")[0].find_element_by_tag_name("td"))


    def getCell(self,rowNo,colNo):
        # 获取表格中某行某列的单元格对象
        try:
            currentRow = self.__table.find_elements_by_tag_name("tr")[rowNo-1]
            currentCol = currentRow.find_elements_by_tag_name("td")[colNo-1]
            return currentCol
        except Exception as e:
            print(e)


    def getWebElementInCell(self,rowNo,colNo,by,value):
        try:
            currentRow = self.__table.find_elements_by_tag_name("tr")[rowNo-1]
            currentCol = currentRow.find_elements_by_tag_name("td")[colNo - 1]
            element = currentCol.find_element(by=by,value=value)
            return element
        except Exception as e:
            print(e)





