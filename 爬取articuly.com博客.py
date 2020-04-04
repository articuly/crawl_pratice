import requests
from bs4 import BeautifulSoup as bs

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.3 Safari/537.36'}


def detail_url(url):
    html = requests.get(url, headers=headers)
    soup = bs(html.text, 'lxml')
    title = soup.title.text[:-7]
    author = soup.select('.vcard .fn a')[0].text
    category = soup.select('.fusion-meta-info-wrapper .updated')[0].text
    tags = soup.select('.meta-tags a')[0].text
    content = soup.select('.post-content')
    print(title, author, category, tags, content)


def craw():
    for page in range(1, 3):
        html = requests.get('https://articuly.com/page/{}/'.format(page), headers=headers)
        soup = bs(html.text, 'lxml')
        articles = soup.select('.fusion-post-content.post-content')
        for article in articles:
            url = article.select('.entry-title.fusion-post-title a')[0]['href']
            detail_url(url)


if __name__ == '__main__':
    craw()
