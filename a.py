# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia  
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-04-01 13:34:07
# @Last Modified time: 2016-07-07 22:13:28
# @FileName: a.py
# 合并中文英文

en = '3B - 18 - Adjust Price With Toppings - Solution.en.srt'
ch = '3B-18-Adjust Price With Toppings - Solution.zh-CN.srt'
fen = open(en)
fch = open(ch)

cnt = 0
chlines = fch.readlines()
for l in fen.readlines():
    cnt += 1
    if cnt % 4 == 3:
        print chlines[cnt-1],
    print l,
