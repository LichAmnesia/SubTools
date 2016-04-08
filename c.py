en = 'input'
# ch = '3A-26-Call Methods on Object.zh-CN.srt'
fen = open(en)
# fch = open(ch)

cnt = 0
# chlines = fch.readlines()
chtmp = '\n'
lines = fen.readlines()
for l in lines:
    cnt += 1
    if cnt % 5 == 3:
        if cnt + 4 < len(lines):
        	print lines[cnt + 4],
        else :
        	print ''
        # chtmp = l
        continue
        # print chlines[cnt-1],
    print l,
