import networkx as nx                   #导入networkx包
import matplotlib.pyplot as plt 
from ipdb import set_trace 
import pandas
import os

def createGraph(filename, G) :
    

    df = pandas.read_excel(filename,
                       sheetname='Sheet1',
                       header=0)
    l = len(df)
    i = 0
    
    while i<l:
        if df[5][i] > 1:
         n1 = df[0][i]
         n2 = df[4][i]
         node_group.append(n2)           
         weight = df[5][i]     
         G.add_weighted_edges_from([(n1, n2, weight)])
        i = i+1        
    return G
    
if __name__=='__main__':
   file_init = '政治'
   ii = 0;
   node_group = ['政治']
   G = nx.Graph()
   plt.figure(1, figsize=(80,80))
   old_node = set()
   while ii<len(node_group):
      # set_trace()
      
      file_init = node_group[ii]
      if file_init not in old_node:
          if os.path.isfile(file_init+'_intext.xlsx'):
             G = createGraph(file_init+'_intext.xlsx', G)
             old_node.add(file_init)
             if (ii == 3) or (ii == 5):
              G1 = nx.Graph()
              G1 = G
              nx.draw(G1, font_family='SimHei', pos = nx.spring_layout(G), alpha = 0.6, node_size = 1, font_color = 'red', with_labels=True)  # , with_labels=True
              plt.savefig(file_init+".png")           
              print(file_init)
              print(ii)   
      ii = ii+1
   #nx.draw(G)
   #plt.savefig("ba.png")
   nx.draw(G, font_family='SimHei', pos = nx.spring_layout(G), alpha = 0.6, node_size = 1, font_color = 'red', with_labels=True)  # , with_labels=True
   plt.savefig(file_init+'final_'+".png")           
   plt.show() 