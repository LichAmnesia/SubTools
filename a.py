# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia  
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-04-01 13:34:07
# @Last Modified time: 2016-04-08 18:27:23
# @FileName: a.py

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
