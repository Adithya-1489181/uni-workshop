import requests
from bs4 import BeautifulSoup
import re
res = requests.get('https://blog.python.org/blog/')
soup = BeautifulSoup(res.content, 'html5lib')
data=soup.find(re.compile(r'div'),attrs={'class':"divide-y divide-zinc-200 dark:divide-zinc-800"})
title_list=[]
author_list=[]
date_list=[]
tempstring=""
for row in data.find_all("article"):
    title_list.append(row.h3.text)
    date_list.append(row.time.text)
    for a in row.find("a",attrs={'class':"font-medium text-zinc-600 hover:text-[#306998] dark:text-zinc-300 dark:hover:text-[#ffd43b] transition-colors"}):
      author_list.append(a.text)
for i in range(len(title_list)):
    tempstring="title: "+title_list[i]+"\nAuthor: "+author_list[i]+"\nDate: "+date_list[i]+"\n----------------\n"
    print(tempstring)
