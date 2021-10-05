# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:25:57 2021

@author: Nitish
"""

class Node:
    def __init__(self,name,country='India'):
        self.__name=name
        self.__country=country
    def get_name(self):
        return self.__name
    def get_country(self):
        return self.__country
    def set_name(self,name):
        self.__name=name
    def set_country(self,country):
        self.__country=country

class Linked_list():
    def __init__(self,head=None):
        self.__head=None
        self.__next=None
        self.__prev=None
    def get_head(self):
        return self.__head
    def add_node(self,data):
        node=Node(data)
        if self.__head==None:
            self.__head=node
        else:
            temp=self.__head
            while temp:
                temp=temp.__next
            temp.__next=node