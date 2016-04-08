en = 'input'
# ch = '3A-26-Call Methods on Object.zh-CN.srt'
fen = open(en)
# fch = open(ch)

cnt = 0
# chlines = fch.readlines()
chtmp = '\n'
for l in fen.readlines():
    cnt += 1
    if cnt % 5 == 3:
        print chtmp,
        chtmp = l
        continue
        # print chlines[cnt-1],
    print l,
