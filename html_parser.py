import re
import urlparse
from bs4 import BeautifulSoup
class HtmlParser(object):
    def parser(self,url,html_content):
        self.soup=BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        self.url=url
        urls=self.getUrls()
        data=self.getData()
        return urls,data
    def getUrls(self):
        #href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8"
        new_urls=set()
        links=self.soup.findAll('a',href=re.compile(r'/item/'))
        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(self.url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def getData(self):
        data={}
        data['tittle']=self.soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        data['text'] = self.soup.find('div', class_='lemma-summary').get_text()
        data['url']=self.url
        return data