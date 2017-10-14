class HtmlOutputer(object):
    def __init__(self):
        self.data=[]
    def collectData(self,data):
        if data is None:
            return
        self.data.append(data)
    def outputHtml(self):
        fout=open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<div>')
        for data in self.data:
            fout.write('<p>%s</p>' % data['url'].encode('utf-8'))
            fout.write('<h3>%s</h3>' % data['tittle'].encode('utf-8'))
            fout.write('<p>%s</p>' % data['text'].encode('utf-8'))
        fout.write('</div>')
        fout.write('</body>')
        fout.write('</html>')