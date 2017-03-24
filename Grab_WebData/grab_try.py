# coding:utf-8
'''
Created on 2016/6/13

@author: sunyihuan
'''
from bs4 import BeautifulSoup
import requests
import lxml

soup = open("adposter_edit.html", 'r')
soup = BeautifulSoup(open('adposter_edit.html'), 'lxml')
head = soup.head.link
tag = soup.div

css_soup = BeautifulSoup('<p class="body strikeout" ></p>', 'lxml')

print head
print css_soup.p["class"]
print tag.name, tag.attrs
# print soup
