# encoding = utf - 8
from DateUtil import currentTime,currentDate
import os

'''
本文件用于存放截图
'''

def createDir():
    # 获得当前文件所在目录的绝对路径
    currentPath = os.path.dirname(os.path.abspath(__file__))
    # 获取今天的日期字符串
    today = currentDate()
    # 构造以日期命名的目录的绝对路径
    dateDir = os.path.join(currentPath,today)
    print(dateDir)
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    # 获取当前时间字符串
    now = currentTime()
    # 构造以当前时间命名的目录的绝对路径
    timeDir = os.path.join(dateDir,now)

    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
        return timeDir

if __name__ == '__main__':
    createDir()
