#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib2
import re
import time
from bs4 import BeautifulSoup
from distutils.filelist import findall
import sys

def weibo():
    # output weibo rank
    # link = 'https://m.weibo.cn/p/231219_2793_newartificial_1001'
    web_file = open('src/rank-weibo.txt')
    contents = web_file.read()
    soup = BeautifulSoup(contents,"html.parser")
    print("创造101 微博打call榜")
    rank_dic = {}
    for tag in soup.find_all('div', class_='m-text-box'):
        name = tag.find('h3', class_='m-text-cut-2').get_text()
        score = int(tag.find('span', class_='txta').get_text().split()[0])
        rank_dic[score] = name
        
    sorted_scores = sorted(rank_dic.keys(), reverse=True)
    count = 0
    for sorted_score in sorted_scores:
        count += 1
        print('#'),
        print(count),
        print(rank_dic[sorted_score]),
        print(':'),
        print(sorted_score)
        if rank_dic[sorted_score] == '吴芊盈':
            output = (sorted_score, count)

    print('------------\n')
    return output

def xiaohongshu():
    # output xiaohongshu rank
    # link = 'https://pages.xiaohongshu.com/activity/produce101?idolid=105&xhs_campaign=000003'
    web_file = open('src/rank-xiaohongshu.txt')
    contents = web_file.read()
    soup = BeautifulSoup(contents,"html.parser")
    print("创造101 小红书pick榜")
    count = 0
    for tag in soup.find_all('div', class_='user-msg'):
        name = tag.find('p', class_='user-name').get_text()
        score = tag.find('p', class_='popularity-value').get_text()
        count += 1
        print('#'),
        print(count),
        print(name),
        print(':'), 
        print(score[:score.find('人气值')])
        if name == '吴芊盈':
            output = (int(score[:score.find('人气值')]), count)
    print('------------\n')
    return output

def doki():
    # output doki info
    page = urllib2.urlopen('http://v.qq.com/biu/doki_personal/index?fantuanId=51661568&starId=1661568&doki_type=0&ptag=4_6.1.1.21692_wxf')
    contents = page.read()
    soup = BeautifulSoup(contents,"html.parser")
    print("创造101 腾讯视频doki")
    rank = soup.find('div', class_='star_info').find('div', class_='item')
    rank_info = int(rank.find('strong', class_='num').get_text())
    print(rank.find('span', class_='label').get_text()),
    print(rank_info)
    rank = soup.find('div', class_='star_info').find('div', class_='item goApp')
    fans = rank.find('strong', class_='num').get_text()
    print(rank.find('span', class_='label').get_text()),
    print(fans)

    # postcard rank
    # link = 'https://m.v.qq.com/app/doki/activity/map/#/?activeId=7&dokiId=51661568&ptag=4_6.1.1.21692_wxf'
    print('\ndoki明信片信箱排行榜')
    web_file = open('src/rank-doki.txt')
    contents = web_file.read()
    soup = BeautifulSoup(contents,"html.parser")
    print(soup.find('div', class_='doki_name').get_text()),
    print(soup.find('span', class_='doki_desc_rank').get_text()),
    print(int(soup.find('span', class_='letter_count').get_text()))

    top = soup.find('div', class_='mod_rank_box')
    top_list = []
    for tag in top.find_all('div', class_='name'):
        top_list.append(tag.get_text())
    print('# 1-11'),
    for name in top_list:
        print(name),
        if name == '吴芊盈':
            output = score[:score.find('票')]
    print('')
    count = 11
    for tag in soup.find_all('div', class_='rank_list rank_list_normal'):
        name = tag.find('span', class_='txt').get_text()
        score = tag.find('span', class_='num').get_text()
        score = int(score[:score.find('封')])
        count += 1
        print('#'),
        print(count),
        print(name),
        print(':'),
        print(score)
        if name == '吴芊盈':
            output = (score, count)
    print('------------\n')
    return (rank_info, fans, output[0], output[1])

def qqmusic():
    # output qqmusic rank
    # link = 'https://y.qq.com/m/act/chuangzao101/v1/list.html?type=rank'
    web_file = open('src/rank-qqmusic.txt')
    contents = web_file.read()
    soup = BeautifulSoup(contents,"html.parser")
    print("创造101 qq音乐人气歌手榜")
    count = 0
    for tag in soup.find_all('li', class_='singer_list__item'):
        name = tag.find('h2', class_='singer_list__tit c_txt3').get_text()
        score = tag.find('p', class_='singer_list__poll c_txt3').get_text()
        count += 1
        print('#'),
        print(count),
        print(name),
        print(':'),
        print(score[:score.find('票')])
        if name == '吴芊盈':
            output = (int(score[:score.find('票')]), count)
    print('------------\n')
    return output

def brief(weibo_result, xiaohongshu_result, doki_result, qqmusic_result):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    complete_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    output_file = open('result/weibo-%s.txt'%date, 'w')
    data = '#创造101吴芊盈 #吴芊盈\n\n【实时数据】\n'
    data += '微博超话签到:\n'
    data += 'doki粉丝数: %s   投票排名: %d (截至5月6日12:00)\n'%(doki_result[1], doki_result[0])
    data += 'doki明信片信箱排行榜: %d   排名: %d (截至5月10日12:00)\n'%(doki_result[2], doki_result[3])
    data += '微博打call榜: %d   排名: %d\n'%(weibo_result[0], weibo_result[1])
    data += '小红书pick榜人气值: %d   排名: %d\n'%(xiaohongshu_result[0], xiaohongshu_result[1])
    data += 'qq音乐人气歌手榜: %d   排名: %d\n'%(qqmusic_result[0], qqmusic_result[1])
    data += '\n【以上数据截止到%s】\n'%str(complete_time)
    output_file.write(data)
    output_file.close()

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    args = sys.argv[1:]
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    clock = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(date),
    print('数据汇总')
    print('截止到'),
    print(clock)
    print('=======================')

    if not args:
        print 'usage: [--complete/--weibo/--xiaohongshu/--doki/--qqmusic] > output file'
        sys.exit(1)
    if args[0] == '--complete':
        weibo_result = weibo()
        xiaohongshu_result = xiaohongshu()
        doki_result = doki()
        qqmusic_result = qqmusic()
        brief(weibo_result, xiaohongshu_result, doki_result, qqmusic_result)
    if args[0] == '--weibo':
        weibo()
    if args[0] == '--xiaohongshu':
        xiaohongshu()
    if args[0] == '--doki':
        doki()
    if args[0] == '--qqmusic':
        qqmusic()

if __name__ == '__main__':
    main()
