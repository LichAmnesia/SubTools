en = 'Relative to Other Views.en.srt'
ch = '1B-16-Relative to Other Views.zh-CN.srt'
fen = open(en)
fch = open(ch)

cnt = 0
chlines = fch.readlines()
for l in fen.readlines():
    cnt += 1
    if cnt % 4 == 3:
        print chlines[cnt-1],
    print l,
