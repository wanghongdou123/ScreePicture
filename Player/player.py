# encoding = utf-8
import unittest
from selenium import webdriver
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_HTML5videoPlayer(self):
        url = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_video_simple"
        self.driver.get(url)
        # print(self.driver.page_source)
        videoPlayer = self.driver.find_element_by_tag_name("video")
        # 获取视频文件网络存储地址
        videoSrc = self.driver.execute_script("return arguments[0].curentSrc;",videoPlayer)
        print(videoSrc)
        # 断言视频存放地址是否符合预期
        # self.assertEqual(videoSrc,"http://www.w3school.com.cn/i/movie.ogg")
        # 获取文件播放时长
        videoDuration = self.driver.execute_script("return arguments[0].duration;",videoPlayer)
        print(videoDuration)
        self.assertEqual(int(videoDuration),3)
        # 播放影片
        self.driver.execute_script("return arguments[0].play();",videoPlayer)
        time.sleep(2)
        # 暂停3秒
        self.driver.execute_script("return arguments[0].pause();",videoPlayer)
        time.sleep(3)
        self.driver.save_screenshot("test.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

