# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-07-07 22:13:34
# @Last Modified time: 2016-07-07 22:15:05
# @FileName: d.py
# 合并中文到英文原字幕文件上

en = 'a.srt'
ch = 'zh.in'
fen = open(en)
fch = open(ch)

cnt = 0
chlines = fch.readlines()
chcnt = 0
for l in fen.readlines():
    cnt += 1
    if cnt % 4 == 3:
        print chlines[chcnt],
        chcnt += 1
    print l,
