# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:42:10 2016

@author: lujinghui
"""

import urllib.request as rq
import xml.etree.ElementTree as tree
import csv




try:

    #two rss links one's topic is sport another is business
    link_rte='http://www.rte.ie/rss/sport.xml'
    link_bbc='http://feeds.bbci.co.uk/news/business/rss.xml'
   
    #use agent to get connect to rte rss url which is related to sport news
    req = rq.Request(link_rte, headers={'User-Agent': 'Mozilla/5.0'})
    response = rq.urlopen(req)
    doc = tree.parse(response)
    
    #save the data into a csv file 
    with open('sport-raw.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for item in doc.iterfind('channel/item'):#parse the feed, extract the description
             description = item.findtext('description')
             writer.writerow(["sport",description]) #append the description of each news and assign a 'sport' label to each row
             
    #use agent to get connect to bcc rss url which is related to business news
    req = rq.Request(link_bbc, headers={'User-Agent': 'Mozilla/5.0'})
    response = rq.urlopen(req)
    doc = tree.parse(response)

    #save the data into a csv file
    with open('business-raw.csv', 'a',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for item in doc.iterfind('channel/item'):#parse the feed, extract the description
             description = item.findtext('description')
             writer.writerow(["business",description]) #append the description of each news assign a 'business' label to each row
    
  

except BaseException as e:
    print("Error: %s" % str(e))