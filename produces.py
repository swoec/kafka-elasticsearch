#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:31:35 2018

@author: alex
"""
from kafka import KafkaProducer
from kafka.errors import KafkaError
import csv 

class prodeces:
    
    def init(self):
        produce = None
        try:
            produce =  KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        except Exception as ex:
            print("error in connect to kafka")
        finally:
            return produce
        
    def readCSV(self,path):
       lines = []
       csvfile = open(path,'rt',encoding='utf-8') 
       spamreader = csv.reader(csvfile)       
       for row in spamreader:
           print(row)
           lines.append(str(row))
         
       return lines
   
    def produceMessages(self,produce,topic, keys, line):
      try:  
        key_bytes = bytes(keys, encoding='utf-8')
        value_bytes = bytes(line, encoding='utf-8')
        produce.send(topic,key=key_bytes,value=value_bytes)
        produce.flush()
        print("messages publish")
      except Exception as ex:
          print("Exception in publishing")
          print(str(ex))
          
if __name__ == '__main__':
     topic = 'testeeeee'
     instances = prodeces()
     producer = instances.init()
     line = instances.readCSV('/home/alex/workspace/Local/ts.csv')
     for i in line: 
         instances.produceMessages(producer,topic,'keyw',i)
     if producer is not None:
            producer.close()
     
          
          
      
           
            
    