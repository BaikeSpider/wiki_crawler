#-*- coding: utf-8 -*-

from langconv import *
from ipdb import set_trace 
import pandas
import types 
import os

def conertit(filename) :

       df = pandas.read_excel(path+"/"+filename,
                       sheetname='Sheet1',
                       header=0)
       l = len(df)
       i = 0
       oldname = filename   
       filename = str(filename)
       # line = filename
       filename = Converter('zh-hans').convert(filename)
       # print(filename)
       # filename = line
       #str(filename)
       #line = line('utf-8')
       line4 = [1]*2500
       line0 = [1]*2500
       line6 = [1]*2500
       # set_trace()    
       while i<l:
            line4[i] = df.loc[i,4]
            line0[i] = df.loc[i,0]
            line6[i] = df.loc[i,6]
            line4[i]=str(line4[i])
            line0[i]=str(line0[i])
            line6[i]=str(line6[i])
            if (df.loc[i,5] == 0):
               df.loc[i,5] = 1
            #if (line4[i] not in old_node):
            #  node_group.append(line4[i]) 
              
            # print(i)
            # if type(line4[i]) == type('a'):
            line4[i] = Converter('zh-hans').convert(line4[i])
            line0[i] = Converter('zh-hans').convert(line0[i])
            line6[i] = Converter('zh-hans').convert(line6[i])

          # line = line.encode('utf-8')
            j = 0
            while j<l:
               if j != i:
                 # set_trace()    
                 xx = df.loc[j,4]
                 xx = str(xx)
                 #print(type(xx))
                 if (type(xx) is type('a')) and (line4[i] is type('a')):
                    if (xx.count(line4[i]) >0) and (df.loc[i,5] > 0):
                      df.loc[i,5]= df.loc[i,5] + df.loc[j,5]
                      #set_trace()    
                      if df.loc[j,4]==line4[i]:
                         # set_trace()   
                         df.loc[j,5] = -1
                    
               j = j+1
            i = i+1
       i = 0
         
       while i<l:
          df.loc[i,4] = line4[i]
          df.loc[i,0] = line0[i]
          df.loc[i,6] = line6[i]
          i= i+1
       bb = pandas.ExcelWriter(path+"/"+filename)  
       df.to_excel(bb) 
       if oldname != filename:
          os.remove(path+"/"+oldname)
       # columnlen = 8
       # cc = 0
       #while cc < columnlen:
       #  df[cc].to_excel(bb) 
       #  cc = cc + 1 
       bb.close()  
       #set_trace()
    
            


if __name__=='__main__':
    ii = 0;
    path = "G:/Python/Baidu-Spider/Encyclopedia_Poject/New"
    node_group = os.listdir(path)
    old_node = set()
    while ii<len(node_group):
      # set_trace()
      file_init = node_group[ii]
      file_init = str(file_init)
      if os.path.splitext(file_init)[1] == '.xlsx':
       if (file_init not in old_node):
         print('read', file_init)
         if os.path.isfile(path+"/"+file_init):
           try: 
            conertit(file_init)  
            print(file_init)
            old_node.add(file_init)
           except: 
            fout = open('record.txt','a', encoding='utf-8')
            fout.write(file_init)
            fout.write('\n')
            fout.close()
      ii = ii +1
      
