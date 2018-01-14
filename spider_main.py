# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer
from ipdb import set_trace
import pandas
import os

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, new_titles, parent, parent_title, parent_all):
        count = 1
        self.outputer.output_randomhtml_init()
        self.urls.add_new_urls(root_url, new_titles, parent, parent_title, parent_all)
        now = 0
        #f = "wiki_output.xlsx"
        #df = pandas.read_excel(f,
        #                       sheet_name='Sheet1',
        #                       header=0)
        #l = len(df)
        #crawled_urls = set()
        #crawled_urls_group = df[1]
        #new_url = 'Mone'
        #for ii in crawled_urls_group:
        #    crawled_urls.add(ii)

        while self.urls.has_new_url():
            try:
                #while new_url in crawled_urls:
                new_url, title, parent_url, parent_title, parent_all, now = self.urls.get_new_url(now)
                #if new_url == 'https://zh.wikipedia.org/wiki/%E6%99%BA%E5%BA%AB':
                #    print('hah')

                # print('crawl %d : %s' % (count, new_url))
                # print(title)
                html_cont = self.downloader.download(new_url)
                # print(html_cont)
                # set_trace()
                new_titles, keyword_times, new_data, new_urls, titles_len, edits, pageviews_url, editors, first_edit, totalviews, category, reference_count, edit_history_url, all_len, words = self.parser.parse(new_url, html_cont, parent_all)
                parent_all = parent_all + '_' + title
                self.urls.add_new_urls(new_urls, new_titles, new_url, title, parent_all)
                # print('mark')
                # self.outputer.collect_data(new_data)
                # set_trace()
                self.outputer.collect_keyword(new_urls, new_titles, new_url, keyword_times, parent_all)
                # set_trace()
                self.outputer.output_txt(title, new_data, words)
                self.outputer.output_html(title, new_url, parent_all)
                self.outputer.output_randomhtml(title, new_url, titles_len, pageviews_url, edits, editors,
                                                first_edit, totalviews, reference_count, category, all_len,
                                                edit_history_url, parent_all)
                #if count == 50000:
                #    break

                count = count + 1

            except:
                print('crawl failed')
                filefail = open ("failedlist.txt",'a', encoding='utf-8')
                filefail.write('crawl failed ')
                filefail.write('%s' % count)
                filefail.write(' ')
                filefail.write('%s' % title)
                filefail.write(' ')
                filefail.write('%s' % new_url)
                filefail.write('\n')
                filefail.write('%s' % parent_title)
                filefail.write(' ')
                filefail.write('%s' % parent_url)
                filefail.write('\n')
                filefail.close()
                self.urls.recover(new_url, title, parent_url, parent_title, parent_all)
        self.outputer.output_randomhtml_finish()


if __name__=='__main__':
    root_url = ['https://zh.wikipedia.org/zh-cn/%E4%BD%93%E8%82%B2%E8%BF%90%E5%8A%A8']
    new_titles = ['体育运动']
    parent = 'Top'
    parent_title = '体育运动'
    parent_all = '体育运动'
    
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, new_titles, parent, parent_title, parent_all)
