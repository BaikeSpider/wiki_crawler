# coding:utf-8
import pandas
import os
from ipdb import set_trace 

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.keywords = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    def collect_keyword(self, new_urls, new_titles, parent, keyword_times, parent_all):
        ii = 0
        self.keywords = []
        while ii < len(new_urls):
            res_keyword = {}
            res_keyword['url'] = new_urls[ii]
            res_keyword['title'] = new_titles[ii]
            res_keyword['id'] = ii + 1
            res_keyword['parent_url'] = parent
            res_keyword['keyword_time'] = keyword_times[ii]
            res_keyword['parent_all'] = parent_all
            self.keywords.append(res_keyword)
            ii = ii+1
    
    def output_txt(self, title, new_data):
        if not (os.path.isfile("txt/"+title+'.txt')):
           fout = open("txt/"+title+'.txt','w', encoding='utf-8')
           fout.write(new_data['summary'])
           fout.close()
        else:
           fout = open("txt/"+new_data['parent']+'_'+title+'.txt','w',  encoding='utf-8')
           fout.write(new_data['title'])
           fout.write('\n')
           fout.write(new_data['summary'])
           fout.close()
           record = open('samekeywords.txt','a',encoding='utf-8')
           record.write(new_data['parent'])
           record.write('-----')
           record.write('\n')
           record.write(new_data['title'])
           record.write('\n')
           record.close()

           
    def output_html(self, parent_title, new_url, parent_all):
        # set_trace()
        #if parent_title == 'UTC+05':
        #   set_trace()
        if not (os.path.isfile("html/"+parent_title+'_intext.html')):
           filename = parent_title
        else:
           filename = parent_all
           
        fout = open("html/"+filename+'_intext.html','w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for keyword in self.keywords:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % parent_title)
            fout.write('<td>%s</td>' % keyword['parent_url'])
            fout.write('<td>%s</td>' % keyword['id'])
            fout.write('<td>%s</td>' % keyword['url'])
            fout.write('<td>%s</td>' % keyword['title'])
            fout.write('<td>%s</td>' % keyword['keyword_time'])
            fout.write('<td>%s</td>' % parent_all)
            fout.write('<td>%s</td>' % parent_all.count('_'))
            fout.write('</tr>')
        # set_trace()
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
        if len(self.keywords):
            with open("html/"+filename+'_intext.html','r',encoding='utf-8') as f:  
               df = pandas.read_html(f.read()) 
        # print (df[0])  
            bb = pandas.ExcelWriter("xlsx/"+filename+'_intext.xlsx')  
            df[0].to_excel(bb) 
            bb.close()  
