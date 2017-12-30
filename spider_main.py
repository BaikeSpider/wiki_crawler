# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer
from ipdb import set_trace 
import os

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, new_titles, parent, parent_title, parent_all):
        count = 1
        self.urls.add_new_urls(root_url, new_titles, parent, parent_title, parent_all)
        now = 0
        while self.urls.has_new_url():
            try:
                new_url, title, parent_url, parent_title, parent_all, now = self.urls.get_new_url(now)
                print('crawl %d : %s' % (count, new_url))
                print(title)
                html_cont = self.downloader.download(new_url)
                # print(html_cont)
                # set_trace()
                new_urls, new_titles, new_data, keyword_times = self.parser.parse(new_url, html_cont, parent_all)
                parent_all = parent_all + '_' + title
                self.urls.add_new_urls(new_urls, new_titles, new_url, title, parent_all)
                # print('mark')
                # self.outputer.collect_data(new_data)
                # set_trace()
                self.outputer.collect_keyword(new_urls, new_titles, new_url, keyword_times, parent_all)
                # set_trace()
                self.outputer.output_txt(title, new_data)
                self.outputer.output_html(title, new_url, parent_all)
                if count == 50000:
                    break

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



if __name__=='__main__':
    root_url = ['https://zh.m.wikipedia.org/zh-cn/%E5%9C%B0%E7%90%86%E5%A4%A7%E7%99%BC%E7%8F%BE',	'https://zh.m.wikipedia.org/zh-cn/%E7%B6%93%E6%BF%9F%E5%85%A8%E7%90%83%E5%8C%96',	'https://zh.m.wikipedia.org/zh-cn/%E8%B3%87%E6%9C%AC%E4%B8%BB%E7%BE%A9%E6%94%BF%E6%B2%BB%E7%B6%93%E6%BF%9F%E5%AD%B8',	'https://zh.m.wikipedia.org/zh-cn/%E5%9C%B0%E7%B7%A3%E6%94%BF%E6%B2%BB%E5%AD%B8',	'https://zh.m.wikipedia.org/zh-cn/1917%E5%B9%B4',	'https://zh.m.wikipedia.org/zh-cn/%E5%8D%81%E6%9C%88%E9%9D%A9%E5%91%BD',	'https://zh.m.wikipedia.org/zh-cn/%E5%85%B1%E7%94%A2%E4%B8%BB%E7%BE%A9%E5%9C%8B%E5%AE%B6',	'https://zh.m.wikipedia.org/zh-cn/%E9%A9%AC%E5%85%8B%E6%80%9D%E4%B8%BB%E4%B9%89',	'https://zh.m.wikipedia.org/zh-cn/%E9%98%B6%E7%BA%A7%E6%96%97%E4%BA%89',	'https://zh.m.wikipedia.org/zh-cn/%E6%96%97%E4%BA%89',	'https://zh.m.wikipedia.org/zh-cn/%E8%B3%87%E7%94%A2%E9%9A%8E%E7%B4%9A',	'https://zh.m.wikipedia.org/zh-cn/%E6%97%A0%E4%BA%A7%E9%98%B6%E7%BA%A7',	'https://zh.m.wikipedia.org/zh-cn/%E6%97%A0%E4%BA%A7%E9%98%B6%E7%BA%A7%E5%9B%BD%E9%99%85%E4%B8%BB%E4%B9%89',	'https://zh.m.wikipedia.org/zh-cn/%E7%90%86%E8%AB%96',	'https://zh.m.wikipedia.org/zh-cn/%E5%85%A7%E6%94%BF',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E7%AD%96',	'https://zh.m.wikipedia.org/zh-cn/%E6%9D%B1%E6%AD%90',	'https://zh.m.wikipedia.org/zh-cn/%E5%85%B1%E7%94%A2%E4%B8%BB%E7%BE%A9%E5%9C%8B%E5%AE%B6',	'https://zh.m.wikipedia.org/zh-cn/%E8%98%87%E8%81%AF',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%B9%E9%9D%A9%E5%BC%80%E6%94%BE',	'https://zh.m.wikipedia.org/zh-cn/%E9%82%93%E5%B0%8F%E5%B9%B3',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AD%E5%9C%8B%E7%89%B9%E8%89%B2%E7%A4%BE%E6%9C%83%E4%B8%BB%E7%BE%A9',	'https://zh.m.wikipedia.org/zh-cn/%E8%B6%8A%E5%8D%97%E7%A4%BE%E6%9C%83%E4%B8%BB%E7%BE%A9%E5%85%B1%E5%92%8C%E5%9C%8B',	'https://zh.m.wikipedia.org/zh-cn/%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89%E5%9B%BD%E5%AE%B6',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E9%BB%A8%E6%94%BF%E6%B2%BB',	'https://zh.m.wikipedia.org/zh-cn/%E9%81%B8%E8%88%89',	'https://zh.m.wikipedia.org/zh-cn/%E6%8A%97%E8%AD%B0',	'https://zh.m.wikipedia.org/zh-cn/%E6%84%8F%E8%AD%98%E5%BD%A2%E6%85%8B',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E7%B6%B1',	'https://zh.m.wikipedia.org/zh-cn/%E5%9B%BD%E5%AE%B6%E6%94%BF%E6%9D%83',	'https://zh.m.wikipedia.org/zh-cn/%E5%86%9B%E4%BA%8B%E6%94%BF%E5%8F%98',	'https://zh.m.wikipedia.org/zh-cn/%E5%9F%B7%E6%94%BF%E9%BB%A8',	'https://zh.m.wikipedia.org/zh-cn/%E5%9C%A8%E9%87%8E%E9%BB%A8',	'https://zh.m.wikipedia.org/zh-cn/%E5%8F%8D%E5%AF%B9%E5%85%9A',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E9%BB%A8%E9%AB%94%E7%B3%BB',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%80%E5%85%9A%E7%8B%AC%E8%A3%81%E5%88%B6',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%80%E5%85%9A%E4%BC%98%E5%8A%BF%E5%88%B6',	'https://zh.m.wikipedia.org/zh-cn/%E5%85%A9%E9%BB%A8%E5%88%B6',	'https://zh.m.wikipedia.org/zh-cn/%E5%A4%9A%E5%85%9A%E5%88%B6',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E5%85%89%E8%AD%9C',	'https://zh.m.wikipedia.org/zh-cn/%E5%B7%A6%E6%B4%BE%E5%92%8C%E5%8F%B3%E6%B4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E5%82%BE%E5%90%91%E6%B8%AC%E8%A9%A6',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E7%BE%85%E7%9B%A4',	'https://en.wikipedia.org/wiki/Pournelle_chart',	'https://zh.m.wikipedia.org/zh-cn/%E5%B7%A6%E6%B4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E7%A4%BE%E6%9C%83%E4%B8%BB%E7%BE%A9',	'https://zh.m.wikipedia.org/zh-cn/%E5%8F%B3%E6%B4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E4%BF%9D%E5%AE%88%E4%B8%BB%E7%BE%A9',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AD%E9%96%93%E6%B4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E8%AB%BE%E8%98%AD%E6%9B%B2%E7%B7%9A',	'https://zh.m.wikipedia.org/zh-cn/%E5%A8%81%E6%AC%8A%E4%B8%BB%E7%BE%A9',	'https://zh.m.wikipedia.org/zh-cn/%E8%87%AA%E7%94%B1%E4%B8%BB%E7%BE%A9',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E8%85%90%E6%95%97',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E8%BF%AB%E5%AE%B3',	'https://zh.m.wikipedia.org/zh-cn/%E8%B2%AA%E8%85%90',	'https://zh.m.wikipedia.org/zh-cn/%E8%B3%84%E8%B3%82',	'https://zh.m.wikipedia.org/zh-cn/%E5%88%A9%E7%9B%8A%E8%BC%B8%E9%80%81',	'https://zh.m.wikipedia.org/zh-cn/%E5%8B%92%E7%B4%A2',	'https://zh.m.wikipedia.org/zh-cn/%E8%A3%99%E5%B8%B6%E9%97%9C%E4%BF%82',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E7%8C%AE%E9%87%91',	'https://zh.m.wikipedia.org/zh-cn/%E9%BB%91%E9%87%91',	'https://zh.m.wikipedia.org/zh-cn/%E4%BE%B5%E5%90%9E',	'https://zh.m.wikipedia.org/zh-cn/%E7%AB%8A%E7%9B%9C%E7%B5%B1%E6%B2%BB',	'https://zh.m.wikipedia.org/zh-cn/%E6%B3%95%E6%B2%BB',	'https://zh.m.wikipedia.org/zh-cn/%E9%80%8F%E6%98%8E%E5%BA%A6',	'https://zh.m.wikipedia.org/zh-cn/%E8%B2%AC%E4%BB%BB%E5%88%B6',	'https://zh.m.wikipedia.org/zh-cn/%E7%B5%B1%E8%A8%88%E5%AD%B8',	'https://zh.m.wikipedia.org/zh-cn/%E9%80%8F%E6%98%8E%E5%9C%8B%E9%9A%9B',	'https://zh.m.wikipedia.org/zh-cn/%E6%B8%85%E5%BB%89%E6%8C%87%E6%95%B8',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%B9%E9%BA%A5',	'https://zh.m.wikipedia.org/zh-cn/%E8%8A%AC%E8%98%AD',	'https://zh.m.wikipedia.org/zh-cn/%E7%B4%90%E8%A5%BF%E8%98%AD',	'https://zh.m.wikipedia.org/zh-cn/%E7%BE%8E%E5%9B%BD',	'https://zh.m.wikipedia.org/zh-cn/%E5%AE%AA%E6%B3%95',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E5%88%B6%E5%BA%A6',	'https://zh.m.wikipedia.org/zh-cn/%E8%A1%8C%E4%B8%BA%E4%B8%BB%E4%B9%89',	'https://zh.m.wikipedia.org/zh-cn/%E7%BE%85%E4%BC%AF%C2%B7%E9%81%93%E7%88%BE',	'https://zh.m.wikipedia.org/zh-cn/%E7%BB%8F%E6%B5%8E%E5%AD%A6',	'https://zh.m.wikipedia.org/zh-cn/%E7%94%9F%E4%BA%A7%E5%85%B3%E7%B3%BB',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%96%E7%95%8C%E9%AB%94%E7%B3%BB%E8%AB%96',	'https://zh.m.wikipedia.org/zh-cn/%E4%BE%9D%E8%B3%B4%E7%90%86%E8%AB%96',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AA%E4%BA%BA%E4%B8%BB%E4%B9%89',	'https://zh.m.wikipedia.org/zh-cn/%E5%B8%82%E5%9C%BA',	'https://zh.m.wikipedia.org/zh-cn/%E5%B8%83%E5%9D%8E%E5%8D%97',	'https://zh.m.wikipedia.org/zh-cn/%E5%85%AC%E5%85%B1%E9%81%B8%E6%93%87%E7%90%86%E8%AB%96',	'https://zh.m.wikipedia.org/zh-cn/%E7%A4%BE%E4%BC%9A%E5%88%86%E5%B7%A5%E8%AE%BA',	'https://zh.m.wikipedia.org/zh-cn/%E6%B3%95%E5%AD%A6',	'https://zh.m.wikipedia.org/zh-cn/%E6%B3%95%E5%BE%8B',	'https://zh.m.wikipedia.org/zh-cn/%E6%B3%95%E5%AD%A6%E5%AE%B6',	'https://zh.m.wikipedia.org/zh-cn/%E6%B3%95%E4%BA%BA',	'https://zh.m.wikipedia.org/zh-cn/%E6%96%87%E5%8C%96%E4%BA%BA%E7%B1%BB%E5%AD%A6',	'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB%E5%AD%B8%E5%9F%BA%E6%9C%AC%E4%B8%BB%E9%A1%8C%E5%88%97%E8%A1%A8',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E7%99%BE%E7%A7%91%E5%85%A8%E4%B9%A6',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E7%99%BE%E7%A7%91%E5%85%A8%E4%B9%A6%E5%87%BA%E7%89%88%E7%A4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E4%BA%BA%E6%B0%91%E5%87%BA%E7%89%88%E7%A4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E6%B1%89%E5%A8%9C%C2%B7%E9%98%BF%E4%BC%A6%E7%89%B9',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%8A%E6%B5%B7%E4%BA%BA%E6%B0%91%E5%87%BA%E7%89%88%E7%A4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E5%88%97%E5%AE%81',	'https://zh.m.wikipedia.org/zh-cn/%E5%93%88%E7%BD%97%E5%BE%B7%C2%B7%E6%8B%89%E6%96%AF%E9%9F%A6%E5%B0%94',	'https://zh.m.wikipedia.org/zh-cn/%E5%95%86%E5%8A%A1%E5%8D%B0%E4%B9%A6%E9%A6%86',	'https://zh.m.wikipedia.org/zh-cn/%E4%B8%8A%E6%B5%B7%E8%AF%91%E6%96%87%E5%87%BA%E7%89%88%E7%A4%BE',	'https://zh.m.wikipedia.org/zh-cn/%E8%A9%B9%E5%A7%86%E6%96%AF%C2%B7%E5%B8%83%E5%9D%8E%E5%8D%97',	'https://zh.m.wikipedia.org/zh-cn/%E5%87%AF%E5%B0%94%E6%A3%AE']
    new_titles = ['地理大发现', '经济全球化', '资本主义政治经济学', '地缘政治学', '1917年', '十月革命', '共产主义国家', '马克思主义', '阶级斗争', '斗争', '资产阶级', '无产阶级', '无产阶级国际主义', '理论', '内政', '政策', '东欧', '共产主义国家', '苏联', '中国大陆', '改革开放', '邓小平', '中国特色社会主义', '越南社会主义共和国', '社会主义国家', '政党政治', '选举', '抗议', '意识形态', '政纲', '国家政权', '军事政变', '执政党', '在野党', '反对党', '政党体系', '一党独裁制', '一党优势制', '两党制', '多党制', '政治光谱', '左派和右派', '政治倾向测试', '政治罗盘', 'en-Pournelle chart', '左派', '社会主义', '右派', '保守主义', '中间派', '诺兰曲线', '威权主义', '自由主义', '政治腐败', '政治迫害', '贪腐', '贿赂', '利益输送', '勒索', '裙带关系', '政治献金', '黑金', '侵吞', '窃盗统治', '法治', '透明度', '责任制', '统计学', '透明国际', '清廉指数', '丹麦', '芬兰', '新西兰', '美国', '宪法', '政治制度', '行为主义', '罗伯·道尔', '经济学', '生产关系', '世界体系论', '依赖理论', '个人主义', '市场', '布坎南', '公共选择理论', '社会分工论', '法学', '法律', '法学家', '法人', '文化人类学', '政治学基本主题列表', '中国大百科全书', '中国大百科全书出版社', '人民出版社', '汉娜·阿伦特', '上海人民出版社', '列宁', '哈罗德·拉斯韦尔', '商务印书馆', '上海译文出版社', '詹姆斯·布坎南', '凯尔森']

    parent = 'https://zh.m.wikipedia.org/zh-cn/%E6%94%BF%E6%B2%BB'
    parent_title = '政治'
    parent_all = '_政治'
    
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, new_titles, parent, parent_title, parent_all)
