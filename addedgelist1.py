# -*- coding: utf-8 -*-

from ipdb import set_trace
import pandas
import os


def conertit(filename, parent_ID, edge_num):
    df = pandas.read_excel(filename + '_convert.xlsx',
                           sheetname='Sheet1',
                           header=0)
    l = len(df)
    i = 0
    line8 = []
    line9 = []
    noneedge = 'W999999'
    while i < l:
        line = df.loc[i, 4]
        str(line)
        if (line not in edgelist_name) and (type(line) is type('a')):
            node_group.append(line)
            edgelist_name.append(line)
            edge_num = edge_num + 1
            edge_ID = "%06d" % edge_num
            edge_ID = "W" + edge_ID
            edgelist.append(edge_ID)
            # pd = df.DataFrame()
            line8.append(parent_ID)
            line9.append(edge_ID)

        elif (line in edgelist_name) and (type(line) is type('a')):
            edge_num = edgelist_name.index(line)
            line8.append(parent_ID)
            line9.append(edgelist[edge_num])
        else:
            print(line)
            print(i)
            line8.append(parent_ID)
            line9.append(noneedge)
        i = i + 1
    # set_trace()    
    # dd8 = {8 : line8}
    # dd9 = {9 : line9}
    # pandas.DataFrame(dd8)
    df['8'] = line8
    df['9'] = line9
    # df.insert(10, dd8)
    # df.insert(10, dd9)
    bb = pandas.ExcelWriter(filename + '_new.xlsx')
    df.to_excel(bb)
    bb.close()
    return edge_num


if __name__ == '__main__':
    ii = 0
    node_group = ['政治']
    old_node = set()
    edge_num = 1
    edgelist = ['NONE', 'W000001']
    edgelist_name = ['NONE', '政治']
    old_node = set()
    # set_trace()
    while ii < len(node_group):
        file_init = node_group[ii]
        str(file_init)
        if file_init not in old_node:
            print(file_init)
            if os.path.isfile(file_init + '_convert.xlsx'):
                parent = edgelist_name.index(file_init)
                parent_ID = edgelist[parent]
                edge_num = conertit(file_init, parent_ID, edge_num)
                old_node.add(file_init)
        ii = ii + 1
