# -*- coding：utf-8 -*-
# author:MARXCBR time:2019/4/26


import requests
from bs4 import BeautifulSoup
import lxml
import time
import random


class haven:
    def __init__(self,name='marx'):
        # self.main_url='https://alpha.wallhaven.cc/search?q=id%3A1957&page={}'
        self.search=name
        self.main_url='https://alpha.wallhaven.cc/search?q={}&page={}'
        self.session=requests.session()
        self.headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "cookie": "__cfduid=d1bc48e470ea703ef259393d775e2f5361542527467; _pk_ses.1.1f04=1; _pk_id.1.1f04=bfd774c029e9a2e1.1542527473.11.1556277865.1556277657.; wallhaven_session=eyJpdiI6IlhHTzhnNmRFelhMdzBZWDdDdzZuUnVwdEh0M2pyMmN3dWo5dHpKS1orSGM9IiwidmFsdWUiOiJoeFFBb0FkWDN2OWpnTTYzaTRwcjgzekp1andjZmpCZDYrTkZYckVXeFFpK2hMSjh3RU5EMzJaM1RYRzR6RG8wVTNocXlDQ29UMDIrUlM1MUVXSjZlQT09IiwibWFjIjoiNTY1YjMyNzNlNTg3NjA0ZDIxZDAzYTI1MTY2NzQzOTRmNTdkMDg1MjZkMDkwZTVlZmE4Y2U3MTI1MjNjMjFkMSJ9"
        }
        self.number=0

    def download_image(self,download_url):

        with open("./image/marxcbr{}.png".format(self.number),'wb') as f:
            f.write(self.session.get(download_url).content)
            self.number+=1

    def get_raw_image_url(self,aim_url):
        page=self.session.get(aim_url)
        soup=BeautifulSoup(page.text,'lxml')
        # print(soup)
        need_data=soup.find('meta',property="og:image")
        download_url="https:"+need_data.get('content')
        self.download_image(download_url)

        print(need_data,"下载完毕")

        time.sleep(random.randint(1,4))


    def run(self):
        for page in range(1,21):
            get_url=self.main_url.format(self.search,page)
            page_data=self.session.get(get_url,headers=self.headers)
            page_data.encoding=page_data.apparent_encoding
            # next_url=[]
            soup=BeautifulSoup(page_data.text,'lxml')

            temp = soup.find('section',class_='thumb-listing-page')

            all_li=temp.find_all('li')
            for temp in all_li:
                try:
                    next_url=temp.find('a').get('href')
                    print(next_url)
                    self.get_raw_image_url(next_url)
                except:
                    ...

haven("Avengers: Endgame").run()

