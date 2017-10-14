# coding:utf8
import url_manager
import html_downloader
import html_outputer
import html_parser
class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self,url):
        self.urls.add_url(url)
        count=0
        while self.urls.has_urls():
            try:
                newUrl=self.urls.getNewUrl()
                html_content=self.downloader.download(newUrl)
                newUrls,newData=self.parser.parser(newUrl,html_content)
                self.urls.add_urls(newUrls)
                self.outputer.collectData(newData)
                print 'craw %d:%s'% (count,newUrl)
                count=count+1
                if count>100:
                    break
            except:
                print 'craw fail'
        self.outputer.outputHtml()




if __name__=='__main__':
    url='https://baike.baidu.com/item/Python/407313?fr=aladdin'
    spider=SpiderMain()
    spider.craw(url)