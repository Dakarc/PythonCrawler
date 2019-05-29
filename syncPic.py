import requests
from lxml import etree
from urllib import request
import os
import re

def parse_page(url):
    headers = {
        'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。！!]','',alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt+suffix
        request.urlretrieve(img_url,'images/'+filename)
        print("保存了")

def main():
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)

if __name__ == '__main__':
    main()