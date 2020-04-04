from selenium import webdriver
from selenium.common.exceptions import TimeoutException  # 超时错误
from selenium.webdriver.common.by import By  # 自定义选择器
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # 设置等待时间
from urllib.parse import quote  # 汉字转成浏览器能理解的
from pyquery import PyQuery as pq  # 解析页面

KEYWORD = 'ipad'
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(r'D:\Browser\360Chrome\Chrome\Application\chromedriver.exe', options=options)
wait = WebDriverWait(browser, 10)  # 等待10秒


def crawl_page():
    try:
        url = 'https://www.taobao.com/'
        browser.get(url)
    except:
        crawl_page()


def get_products():
    pass


if __name__ == '__main__':
    crawl_page()
