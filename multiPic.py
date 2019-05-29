import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

class Producer():
    header = {
        'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
    }

    def parse_page(self,url):
        response = requests.get(url,headers=self.header)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img  in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.\*，。！!]','',alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            self.img_queue.put((img_url,filename))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'images/ '+filename)
            print(filename+' 下载完成!')
