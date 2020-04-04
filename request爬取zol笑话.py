import requests
from bs4 import BeautifulSoup as bs

# 从源码获取headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.3 Safari/537.36'}
for i in range(1, 4):
    # 首先要观察网址的规律
    html = requests.get('http://xiaohua.zol.com.cn/new/{}.html'.format(i), headers=headers)
    # print(html.text)
    # 解析源码
    soup = bs(html.text, 'lxml')
    print(soup.title)
    # print(soup.head)
    # print(soup.find_all('a'))
    for joke in soup.select('li.article-summary'):
        title = joke.select('.article-title')[0].text
        source = joke.select('.article-source span')[-1].text
        content = joke.select('.summary-text p')[0].text
        print(title, source, content)
