#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:18:09 2018

@author: alex
"""


from elasticsearch import Elasticsearch
from customer import customer
import re

class Indexs:
    es = Elasticsearch() 
    def buildIndx(self):
         instance = customer()
         messages = instance.init()
         reg = re.compile('.*,.*,.*')
         for i in messages:
           #print(i.value)
           item = str(i.value)
           if reg.match(item):
              print(item)
              time,latitude,longtitude = item.split(",")        
              self.es.index(index="event",doc_type="records",id=time,body={"time":time,"latitude":latitude,"longtitude":longtitude})
            
            
    def searchEs(self,time):
        
        ress = self.es.search(index="event",doc_type="records",body={"query": {"match": {"time":time}}})
        
        print("%d documents found" % ress['hits']['total'])
        for hit in ress['hits']['hits']:
            print(hit["_source"])
            print(hit['_source']['time'])
            latitude = hit['_source']['latitude']
            longtitude = hit['_source']['longtitude']
        return ress
            
            
if __name__=='__main__':
     t = Indexs();
     t.buildIndx();
     res = t.searchEs('2013-07-10 02:52:49');
     for i in res:
         print("feedback----")
         print(i);

