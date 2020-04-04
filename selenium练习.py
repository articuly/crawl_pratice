from selenium import webdriver

# browser=webdriver.Firefox(r'D:\Browser\Firefox\geckodriver.exe')
browser = webdriver.Chrome(r'D:\Browser\Chromium\chromedriver.exe')
browser.get('http://www.baidu.com')
search_box = browser.find_element_by_id('kw')
search_box.send_keys('python')
submit_button = browser.find_element_by_id('su')
submit_button.click()
