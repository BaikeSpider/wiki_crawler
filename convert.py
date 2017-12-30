#-*- coding: utf-8 -*-

from langconv import *
from ipdb import set_trace 
import pandas
import types 
import os

def conertit(filename) :
   
       df = pandas.read_excel(filename+'_intext.xlsx',
                       sheetname='Sheet1',
                       header=0)
       l = len(df)
       i = 0
       str(filename)
       line = filename
       line = Converter('zh-hans').convert(line)
       # print(filename)
       filename = line
       #str(filename)
       #line = line('utf-8')
       line4 = [1]*2500
       line0 = [1]*2500
       line6 = [1]*2500
       
       while i<l:
          if (df.loc[i,5] != 0):
            line4[i] = df.loc[i,4]
            line0[i] = df.loc[i,0]
            line6[i] = df.loc[i,6]
            str(line4[i])
            str(line0[i])
            str(line6[i])
            if (line4[i] not in old_node) and (type(line4[i]) is type('a')):
              node_group.append(line4[i]) 
            # print(i)
            if type(line4[i]) is type('a'):
              line4[i] = Converter('zh-hans').convert(line4[i])
            line0[i] = Converter('zh-hans').convert(line0[i])
            line6[i] = Converter('zh-hans').convert(line6[i])

          # line = line.encode('utf-8')
            j = 0
            while j<l:
               if j != i:
                 # set_trace()    
                 xx = df.loc[j,4]
                 str(xx)
                 #print(type(xx))
                 if (type(xx) is type('a')) and (line4[i] is type('a')):
                    if (xx.count(line4[i]) >0) and (df.loc[i,5] != 0):
                      df.loc[i,5]= df.loc[i,5] + df.loc[j,5]
                      #set_trace()    
                      if df.loc[j,4]==line4[i]:
                         # set_trace()   
                         df.loc[j,5] = 0
                
               j = j+1
          i = i+1
       i = 0
         
       while i<l:
          df.loc[i,4] = line4[i]
          df.loc[i,0] = line0[i]
          df.loc[i,6] = line6[i]
          i= i+1
       bb = pandas.ExcelWriter(filename+'_intext.xlsx')  
       df.to_excel(bb) 
       # columnlen = 8
       # cc = 0
       #while cc < columnlen:
       #  df[cc].to_excel(bb) 
       #  cc = cc + 1 
       bb.close()  
       #set_trace()
       


if __name__=='__main__':
    file_init = 'Pournelle chart'
    ii = 0;
    node_group = ['政治']
    old_node = set()
    while ii<len(node_group):
      # set_trace()
      file_init = node_group[ii]
      str(file_init)
      if file_init not in old_node:
         print(file_init)
         if os.path.isfile(file_init+'_intext.xlsx'):
            conertit(file_init)  
            old_node.add(file_init)             
      ii = ii +1
      
