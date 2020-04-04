import requests
from bs4 import BeautifulSoup as bs

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.3 Safari/537.36'}


def detail_url(url):
    html = requests.get(url, headers=headers)
    soup = bs(html.text, 'lxml')
    title = soup.title.text[:-6]
    company_name = soup.select('.com_intro .com-name')[0].text
    city = soup.select('.job_msg .job_position')[0].text
    # 字体编码破解
    salary = soup.select('.job_money.cutom_font')[0].text.encode('utf-8')
    salary = salary.replace(b'\xef\xa0\x8b', b'0')
    salary = salary.replace(b'\xef\x9b\x9e', b'1')
    salary = salary.replace(b'\xee\xb0\xbf', b'2')
    salary = salary.replace(b'\xee\xbb\x89', b'8')
    salary = salary.replace(b'\xef\x88\xa0', b'5')
    salary = salary.replace(b'\xee\xb3\xab', b'3')
    salary = salary.replace(b'\xee\xa4\xa9', b'4')
    salary = salary.decode()
    print(title, company_name, city, salary)


def craw():
    for page in range(1, 4):
        html = requests.get(
            'https://www.shixiseng.com/interns?page={}&keyword=python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='.format(
                page),
            headers=headers)
        soup = bs(html.text, 'lxml')
        offers = soup.select('.intern-wrap.intern-item')
        for offer in offers:
            url = offer.select('.f-l.intern-detail__job a')[0]['href']
            detail_url(url)


if __name__ == '__main__':
    craw()
