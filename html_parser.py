# coding:utf-8
import bs4
from bs4 import BeautifulSoup
import re
import html_downloader
import requests
import json
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import quote
from urllib.request import urlopen
from ipdb import set_trace
from ipdb import set_trace 
from langconv import *


class HtmlParser(object):
    @staticmethod
    def replaceillgalchar(link_text):
        # set_trace()
        while link_text.find(':')>=0:
          # 
          link_text = link_text.replace(':', '-')
        while link_text.find('?')>=0:
          link_text = link_text.replace('?', '-')
        while link_text.find('<')>=0:
          link_text = link_text.replace('<', '-')
        while link_text.find('>')>=0:
          link_text = link_text.replace('>', '-')
        while link_text.find('|')>=0:
          link_text = link_text.replace('|', '-')       
        while link_text.find(r'\\')>=0:
          link_text = link_text.replace(r'\\', '-')  
        while link_text.find('\/')>=0:
          # set_trace()
          link_text = link_text.replace(r'\/', '-')  
        return link_text
    def _get_new_urls(self, page_url, soup):
        #def has_class_and_text(tag):
        #   return tag['class'] == 'references'
        #def has_class_but_no_id(tag):
        #   return tag.has_attr('class')
        new_urls = []
        new_titles = []
        keyword_times = []
        # /view/123.htm
        # links = soup.find_all('a', href=re.compile(r'/view/[\u4e00-\u9fa5]+'))
        # set_trace()

        #categories crawl
        categories = soup.find("div", class_="mw-normal-catlinks")
        category = []
        if categories is None:
            category.append("None_Category!!!")
        else:
            for child in categories.contents[2].contents:
                category.append(child.text)
            if len(category) == 0:
               category.append("None_Category!!!")

        #references crawl
        references = soup.find_all("ol", class_="references")  # it will find all references, including the references, cites and notes.
        if references is None:
            reference_count = 0
        else:
            reference_count = 0
            for ii in references:
              for child in ii.contents:
                if type(child) is bs4.element.Tag:
                    reference_count += 1

        links_orginal = soup.find_all('a',href=re.compile(r'/wiki/'))
        links = []
        illegalchar = ('*', '+', '-', '?', '.' , ',') 
        deleurl1 = re.compile(r'/wiki/Special:')
        deleurl2 = re.compile(r'/wiki/Category:')
        deleurl3 = re.compile(r'/wiki/%E7%BB%B4%E5%9F%BA%E8%AF%AD%E5%BD%95')
        deleurl4 = re.compile(r'/wiki/Wikipedia:')
        deleurl5 = re.compile(r'/wiki/File:')
        deleurl6 = re.compile(r'/wiki/Template:')
        deleurl7 = re.compile(r'/wiki/Portal:')
        deleurl8 = re.compile(r'/wiki/Privacy_policy')
        deleurl9 = re.compile(r'/wiki/%E7%BB%B4%E5%9F%BA%E5%85%B1%E4%BA%AB%E8%B5%84%E6%BA%90')
        deleurl10 = re.compile(r'/wiki/Help:')
        deleurl11 = re.compile(r'wiktionary\.org')
        deleurl12 = re.compile(r'wikimediafoundation\.org')
        deleurl13 = re.compile(r'wikivoyage\.org')
        deleurl14 = re.compile(r'wikimedia\.org')
        deleurl17 = re.compile(r'wikisource\.org')
        deleurl18 = re.compile(r'wikidata\.org')
        deleurl19 = re.compile(r'wikibooks\.org')
        deleurl20 = re.compile(r'wiki/Project:')
        deleurl15 = re.compile(r'/wiki/Main_Page')
        deleurl16 = re.compile(r'/wiki/Talk:')
        convert = re.compile(r'zh.m.wikipedia\.org/wiki/')
        
        for link in links_orginal:
            #if re.search('\.(jpg|JPG|svg|SVG)$',link['href']):
            #   links.remove(link)
            if not ((re.search(deleurl1, link['href'])) or (re.search(deleurl2, link['href'])) or (
            re.search(deleurl3, link['href'])) or (re.search(deleurl4, link['href'])) or (
            re.search(deleurl6, link['href'])) or (re.search(deleurl5, link['href'])) or (
            re.search(deleurl7, link['href'])) or (re.search(deleurl8, link['href'])) or (
            re.search(deleurl9, link['href'])) or (re.search(deleurl10, link['href'])) or (
            re.search(deleurl11, link['href'])) or (re.search(deleurl12, link['href'])) or (
            re.search(deleurl13, link['href'])) or (re.search(deleurl14, link['href'])) or (
            re.search(deleurl15, link['href'])) or (re.search(deleurl16, link['href'])) or (
            re.search(deleurl17, link['href'])) or (re.search(deleurl18, link['href'])) or (
            re.search(deleurl19, link['href'])) or (re.search(deleurl20, link['href']))):
               links.append(link)
        old_link = set()       
        # set_trace()
        url_parse = urlparse(page_url)
        convert2 = re.compile(r'/zh-cn/')
        if re.search(convert2, url_parse.path):
            url_parse_temp = url_parse.path.replace('/zh-cn/', '/wiki/')
        else:
            url_parse_temp = url_parse.path
        for link in links:
          if (link.text == '') or (link.text == '浏览条目正文[c]') or (link['href'] == url_parse_temp):
             continue
          if link.text == '':
             continue            
          # print(link) # for test
          
          if link['href'].find('#') != -1:
           t = link['href'].find('#')
           link['href'] = link['href'][0:t]
          # link.text = Converter('zh-hans').convert(link.text )  # transform the text
          if link.text not in old_link:
           new_url = link['href']
           new_full_url = urljoin(page_url, new_url)
           if re.search(convert, new_full_url):
             new_full_url = new_full_url.replace('/wiki/','/zh-cn/')
           # set_trace()    
           new_urls.append(new_full_url)
           #if 'title' in link):
           if link.get('title') != None:
               if (link['title'] != ''):
                   textnow = self.replaceillgalchar(link['title'])
                   textnow = textnow.strip()
               else:
                   textnow = self.replaceillgalchar(link.text)
                   textnow = textnow.strip()
           else:
               textnow = self.replaceillgalchar(link.text)
               textnow = textnow.strip()
           new_titles.append(textnow)    
           old_link.add(link.text)
           
           temp = link.text
           if (temp.find('(') != -1):
               temp = temp.replace('(', '\(')
           if (temp.find(')') != -1):
               temp = temp.replace(')', '\)')
           if (temp.find('+') != -1):
               temp = temp.replace('+', '\+')
           if (temp.find('*') != -1):
               temp = temp.replace('*', '\*')
           if (temp.find(' ') != -1):
               temp = temp.replace(' ', '\s')
           if (temp.find('?') != -1):
               temp = temp.replace('?', '\?')
           if (temp.find('{') != -1):
               temp = temp.replace('{', '\{')
           if (temp.find('}') != -1):
               temp = temp.replace('}', '\}')
           temp = temp.strip()
           keyword_time = soup.find_all(string=re.compile(temp))
           keywordtime = 0
           for keyword in keyword_time:
              keywordtime = keywordtime + keyword.count(link.text)
           keyword_times.append(keywordtime)
           
        # set_trace()  
        return len(new_titles), new_urls, new_titles, keyword_times, category, reference_count

    def _get_new_data(self, page_url, soup, parent_all):
        res_data = {}
        # url
        # res_data['url'] = page_url
        
        title_node = soup.find('div', class_='mw-body').find('h1')
        parent_title = title_node.get_text()
        res_data['title'] = parent_title
        summary_node = soup.find(name='p')
        if (summary_node != None):
          if (summary_node.get('text') != None):
            res_data['summary'] = summary_node.get_text()
          else:
            res_data['summary'] = '!!!No summary!!!'       
        else:
          res_data['summary'] = '!!!No summary!!!'     
        res_data['parent'] = parent_all
        # print(res_data)

        # 统计字数
        all_text = soup.find('div', class_='mw-content-ltr')
        catalog_text = soup.find('div', class_='catlinks')
        all_text_len = len(all_text.text)
        catalog_text_len = len(catalog_text.text)
        all_len = all_text_len + catalog_text_len + len(parent_title)  # comprises text, catalog and title
        words = all_text.text + catalog_text.text
        # open the link of article information
        info_link = soup.find_all('a', href=re.compile(r'&action=info'))
        info_url = urljoin(page_url, info_link[0]['href'])
        self.downloader = html_downloader.HtmlDownloader()
        html_cont = self.downloader.download(info_url)
        info_soup = BeautifulSoup(html_cont, 'html.parser')

        # 修订历史统计  http://vs.aka-online.de/cgi-bin/wppagehiststat.pl?lang=zh.wikipedia&page=%E6%94%BF%E6%B2%BB
        edit_history_url_temp = info_soup.find('a', href=re.compile(r'//vs.aka-online.de/cgi-bin/wppagehiststat.pl'))
        edit_history_url = edit_history_url_temp['href']
        # store the edit_histroy_url

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        # 页面详细信息与统计
        articleinfo_url_temp = info_soup.find('a', href=re.compile(r'//tools.wmflabs.org/xtools-articleinfo/index.php'))
        articleinfo_url = 'https:' + articleinfo_url_temp[
            'href']  # https://tools.wmflabs.org/xtools-articleinfo/index.php?article=%E9%98%BF%E7%B1%B3%E4%BB%80%E4%BA%BA&project=zh.wikipedia.org
        articleinfo_cont = requests.get(articleinfo_url, headers=headers)
        articleinfo_soup = BeautifulSoup(articleinfo_cont.text, 'html.parser')
        text1 = articleinfo_soup.find_all('div', class_='col-lg-6 stat-list clearfix')
        if text1[0].find_all('td')[6].text == "Total edits":
            edits = text1[0].find_all('td')[7].text
            editors = text1[0].find_all('td')[9].text
            ip_edits = text1[0].find_all('td')[13].text
        else:
            edits = text1[0].find_all('td')[5].text
            editors = text1[0].find_all('td')[7].text
            ip_edits = text1[0].find_all('td')[11].text
        pos1 = ip_edits.find('·')
        ip_edits = ip_edits[0: pos1]
        ip_edits = ip_edits.strip()
        # ip_edits = ip_edits.rstrip()
        edits = edits.strip()
        editors = editors.strip()
        # edits = edits.rstrip()
        # edits= int(edits)  # remove spaces
        # editors = text1[0].find_all('td')[9].text
        # editors = editors.strip()
        # editors = editors.rstrip()
        p = re.compile(r'\d+,\d+?')
        s = edits
        for m in p.finditer(s):
            mm = m.group()
            s_back = s.replace(mm, mm.replace(',', ''))
            s = s_back
        edits = s

        s = ip_edits
        for m in p.finditer(s):
            mm = m.group()
            s_back = s.replace(mm, mm.replace(',', ''))
            s = s_back
        ip_edits = s

        edits = int(edits) - int(ip_edits)

        # 创建时间
        first_edit = text1[1].find_all('td')[1].text
        pos1 = first_edit.find(',')
        first_edit = first_edit[0: pos1].strip()
        # articleinfo_cont = self.downloader.download(articleinfo_url)
        # articleinfo_soup = BeautifulSoup(articleinfo_cont, 'html.parser')

        # 访问量 Total Views
        pos1 = articleinfo_url_temp['href'].find('article=')
        pos2 = articleinfo_url_temp['href'].find('project=')
        entry_title = articleinfo_url_temp['href'][pos1 + 8: pos2 - 1]
        #  = info_soup.find_all('a',href=re.compile(r'//tools.wmflabs.org/pageviews'))
        pageviews_url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/zh.wikipedia/all-access/all-agents/' + entry_title + '/daily/2000110100/2017112000'
        # pageviws_cont = requests.get(pageviws_url, headers=headers)
        # pageviws_soup = BeautifulSoup(pageviws_cont.text, 'html.parser', from_encoding='utf-8')

        u = requests.get(pageviews_url, headers=headers)
        # u = urlopen(pageviews_url)
        response = json.loads(u.text)
        totalviews = 0
        if len(response) != 1:
            totalviews = 999999999
        else:
            for jj in response['items']:
                totalviews += jj['views']

        return res_data, edits, pageviews_url, editors, first_edit, totalviews, edit_history_url, all_len, words

    def parse(self, page_url, html_cont, parent_all):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # remove the portal of other languages
        if soup.find('div',  id = 'p-lang') is not None:
            soup.find('div', id='p-lang').decompose()
        # print(soup.prettify())G:\Python\Baidu-Spider\Encyclopedia_Poject\Wiki-new-code\html_parser.py
        # set_trace()  
        titles_len, new_urls, new_titles, keyword_times, category, reference_count = self._get_new_urls(page_url, soup)
        new_data, edits, pageviews_url, editors, first_edit, totalviews, edit_history_url, all_len, words = self._get_new_data(page_url, soup, parent_all)
        # print('mark')
        # set_trace()   
        return new_titles, keyword_times, new_data, new_urls, titles_len, edits, pageviews_url, editors, first_edit, totalviews, category, reference_count, edit_history_url, all_len, words
