#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:16:50 2018

@author: alex
"""
from kafka import KafkaConsumer

class customer():
    def init(self):
        customer = None
        topic_name = 'test'
        try:
            customer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
        except Exception as ex:
            print("Exception in customer")
            print(str(ex))
        finally:
            return customer
        
if __name__ == '__main__':
    instance = customer();
    customer = instance.init();
    for i in customer:
        print(i.value);