# coding:utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from urllib.parse import quote
from ipdb import set_trace 



class HtmlParser(object):
   
    def _get_new_urls(self, page_url, soup, old_link):
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
        wikitext = soup.find_all('p')
        i = 0
        # set_trace()
        illegalchar = ('*', '+', '-', '?', '.' , ',')
        while i< len(wikitext):
           links = wikitext[i].find_all('a',href=re.compile(r'^/wiki/'))
           for link in links:
               if re.search('\.(jpg|JPG|svg|SVG)$',link['href']):
                  links.remove(link)
                  
           for link in links:
               if (link.text not in old_link) and (type(link.text) == type('a')) and (link.text not in illegalchar):
                  new_url = link['href']
                  new_full_url = urljoin(page_url, new_url)
                  new_urls.append(new_full_url)
                  new_titles.append(link.text) 
                  old_link.add(link.text)
                  # print(new_full_url)
                  #if i>8:
                  #  set_trace()
                  keyword_time = soup.find_all(string=re.compile(link.text))
                  keywordtime = 0
                  for keyword in keyword_time:
                      keywordtime = keywordtime + keyword.count(link.text)
                  
                  #keyword_time = 0
                  #keywordtime = 0
                  #for wikitext_p in wikitext:
                  #   keyword_time = wikitext_p.find_all(string=re.compile(link.text))
                   #  for keyword in keyword_time:
                   #     keywordtime = keywordtime + keyword.count(link.text)
                  
                  keyword_time = keywordtime
                  keyword_times.append(keyword_time)                

           i = i+1
		# for link in links:
        #set_trace()
        wikitext = soup.find_all('li')
        
        i = 0
        while i< len(wikitext):
           #links = wikitext[i].find_all(has_class_but_no_id)
           # links = has_class_and_text
           links = wikitext[i].find_all('a',href=re.compile(r'^/wiki/'))
           for link in links:
               if re.search('\.(jpg|JPG|svg|SVG)$',link['href']):
                  links.remove(link)           
           for link in links:
               if (link.text not in old_link) and (type(link.text) == type('a')) and (link.text not in illegalchar):
                  new_url = link['href']
                  new_full_url = urljoin(page_url, new_url)
                  new_urls.append(new_full_url)
                  new_titles.append(link.text) 
                  old_link.add(link.text)
                  # print(new_full_url)
                  keyword_time = soup.find_all(string=re.compile(link.text))
                  keywordtime = 0
                  for keyword in keyword_time:
                      keywordtime = keywordtime + keyword.count(link.text)
                  
                  #keyword_time = 0
                  #keywordtime = 0
                  #for wikitext_p in wikitext:
                  #   keyword_time = wikitext_p.find_all(string=re.compile(link.text))
                   #  for keyword in keyword_time:
                   #     keywordtime = keywordtime + keyword.count(link.text)
                  
                  keyword_time = keywordtime
                  keyword_times.append(keyword_time)                

           i = i+1
         
        return new_urls, new_titles, keyword_times, old_link

    def _get_new_data(self, page_url, soup, parent):
        res_data = {}
        # url
        # res_data['url'] = page_url
        
        title_node = soup.find('div', class_='mw-body').find('h1')
        parent_title = title_node.get_text()
        res_data['title'] = parent_title
        summary_node = soup.find(name='p')
        res_data['summary'] = summary_node.get_text()
        res_data['parent'] = parent
        # print(res_data)
        return res_data, parent_title

    def parse(self, page_url, html_cont, parent, old_link):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # print(soup.prettify())
        new_urls, new_titles, keyword_times, old_link = self._get_new_urls(page_url, soup, old_link)
        new_data, parent_title= self._get_new_data(page_url, soup, parent)
        # print('mark')
        return new_urls, new_titles, new_data, parent_title, keyword_times, old_link
