import networkx as nx                   #导入networkx包
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt 
from ipdb import set_trace 
import pandas
import os
import json

def createGraph(filename, G) :
    

    df = pandas.read_excel(filename,
                       sheetname='Sheet1',
                       header=0)
    l = len(df)
    i = 0
    
    if filename == '政治_new.xlsx':
      while i<l:
        if (df[5][i] >= 1):
         if df[4][i] == '':
           continue

         n1 = df[0][i]
         n2 = df[4][i]
         n1 = str(n1)
         n2 = str(n2)
         node_group.append(n2)   
         branch1.append(n2)         
         branch_node.add(n2 + '_new.xlsx')  
         weight = int(df[5][i])
         G.add_weighted_edges_from([(n1, n2, weight)])
         G.nodes[n2]['key'] = 1

        i = i+1        
         
    elif filename in branch_node:
      while i<l:
        if (df[5][i] >= 1):
         if df[4][i] == '':
           continue

         n1 = df[0][i]
         n2 = df[4][i]
         n1 = str(n1)
         n2 = str(n2)
         node_group.append(n2)
         branch2.append(n2)
         weight = int(df[5][i])
         #G.add_nodes_from(n1) //error: repeat addition

         G.add_weighted_edges_from([(n1, n2, weight)])
         G.nodes[n2]['key'] = 2

        i = i+1   
    else:
      while i<l:
        if (df[5][i] >= 1):
         if df[4][i] == '':
           continue
         n1 = df[0][i]
         n2 = df[4][i]
         n1 = str(n1)
         n2 = str(n2)
         node_group.append(n2)         
         branch3.append(n2) 
         weight = int(df[5][i])
         G.add_weighted_edges_from([(n1, n2, weight)])
         G.nodes[n2]['key'] = 3
        i = i+1    

    return G
    
if __name__=='__main__':
   file_init = '政治'
   ii = 0
   node_group = ['政治']
   G = nx.DiGraph()
   old_node = set()
   branch_node = set()
   branch1 = []
   branch2 = []
   branch3 = []
   while ii<len(node_group):

      file_init = node_group[ii]
      if (file_init not in old_node) and (type(file_init) == type('a')):
          if os.path.isfile(file_init+'_intext.xlsx'):
             G = createGraph(file_init+'_intext.xlsx', G)
             old_node.add(file_init)
   
      ii = ii+1
   H = json_graph.node_link_data(G)
   s1 = json.dumps(H)
   fileObject = open('wiki.json', 'w', encoding='utf-8')
   fileObject.write(s1)  
   fileObject.close()
   file1 = open('wiki_branch1.txt', 'w', encoding='utf-8')
   for ii in branch1:
       file1.write(ii)
       file1.write('\n')
   file1.close()
   file2 = open('wiki_branch2.txt', 'w', encoding='utf-8')
   for ii in branch2:
       file2.write(ii)
       file2.write('\n')
   file2.close()
   file3 = open('wiki_branch3.txt', 'w', encoding='utf-8')
   for ii in branch3:
       file3.write(ii)
       file3.write('\n')
   file3.close()