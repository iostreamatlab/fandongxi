# -*- coding: UTF-8 -*-
"""
 获取翻东西网美妆
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 获得指定开始排行
def get_url(root_url,start):
    return root_url+str(start)

def get_review(page_url):
    cooks_list=[]
    response=requests.get(page_url)
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find('div','goods_items')
    for tag_li in soup.find_all('div','deal'):
    
        dict={}
        dict['name']=tag_li.find('h2').find('a','mall_ico').string
        dict['price']=tag_li.find('h4').find('b').string
        dict['already seal']=tag_li.find('h5').find('span').string
        dict['discount']=tag_li.find('h4').find('span','p_prew').find('em','fan_rate').string
        cooks_list.append(dict)
    return cooks_list



if __name__ == "__main__":

#获取翻东西网的数据
#10004:衣服
#10002:美妆
#10003:美食
#10016:鞋包
#10006:数码


    all_lists=[];
    root_url="http://super.fandongxi.com/index.php?mod=goods&act=index&code=super&cid=10006&do=&keywords=&sort=0&page="
    start=1
    while(start<5):
        goods_list=get_review(get_url(root_url,start))
        for good_dict in goods_list:
            print('name:'+good_dict.get('name'))
            print('price:'+good_dict.get('price'))
            print('already seal:'+good_dict.get('already seal'))
            print('discount:'+good_dict.get('discount'))
            print('------------------------------------------------------')
            all_lists.append(good_dict)
        start+=1
        
    print repr(all_lists).decode("unicode–escape")
        



