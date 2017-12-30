# -*- coding: utf-8 -*-

from ipdb import set_trace
import pandas
import os
import re


def conertit(filename, parent_id, edge_num):
    df = pandas.read_excel(filename + '_intext.xlsx',
                           sheetname='Sheet1',
                           header=0)
    l = len(df)
    i = 0
    line8 = []
    line9 = []
    noneedge = 'W9999999'
    wikisouceedge = 'W9999998'
    while i < l:
        line = df.loc[i, 4]
        line = str(line)
        line_url = df.loc[i, 3]
        wikisource = re.compile(r'wikisource\.org')
        wikidata = re.compile(r'wikidata\.org')
        if (line not in edgelist_name) and not (re.search(wikisource, line_url)) and not (re.search(wikidata, line_url)):
            node_group.append(line)
            edgelist_name.append(line)
            edge_num = edge_num + 1
            edge_id = f"{edge_num:07d}"
            edge_id = "W" + edge_id
            edgelist.append(edge_id)
            # pd = df.DataFrame()
            line8.append(parent_id)
            line9.append(edge_id)
        elif (line in edgelist_name) and not (re.search(wikisource, line_url)) and not (re.search(wikidata, line_url)):
            edge_num = edgelist_name.index(line)
            line8.append(parent_id)
            line9.append(edgelist[edge_num])
        else:
            fout = open('failededges.txt', 'a', encoding='utf-8')
            fout.write(parent_id)
            fout.write('\n')
            fout.write(line)
            fout.write('\n')
            fout.write(line_url)
            fout.write('\n')
            fout.close()
            if ((re.search(wikisource, line_url))  or (re.search(wikidata, line_url))) and os.path.isfile(line + '_intext.xlsx'):
                os.remove(line + '_intext.xlsx')
                line8.append(parent_id)
                line9.append(noneedge)
            else:
                line8.append(parent_id)
                line9.append(wikisouceedge)
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
    edgelist = ['W0000001']
    edgelist_name = ['政治']
    old_node = set()

    # set_trace()
    while ii < len(node_group):
        file_init = node_group[ii]
        # str(file_init)
        if file_init not in old_node:
            print(file_init)
            if os.path.isfile(file_init + '_intext.xlsx'):
                parent = edgelist_name.index(file_init)
                parent_id = edgelist[parent]
                edge_num = conertit(file_init, parent_id, edge_num)
                old_node.add(file_init)
            else:
                fout = open('notexistfiles.txt', 'a', encoding='utf-8')
                fout.write(file_init)
                fout.write('\n')
        ii = ii + 1
