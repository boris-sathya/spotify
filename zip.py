import sys
from operator import itemgetter
inp = sys.stdin.readlines()
splits = []
rank = []
songs = {}
i = 0
while len(inp) > i:
    splits = splits + (inp[i].split())
    i = i + 1
#calculate rank using zipf's law
#store ranks in a list

i = 1
while i <= int(splits[0]):
    testval = int(splits[i*2])
    ref = int(splits[2])/i
    q = float(testval)/float(ref)
    meta = []
    meta.append(splits[(i*2)+1])
    meta.append(i)
    ranked_meta = []
    ranked_meta.append(q)
    ranked_meta.append(meta)
    rank.append(ranked_meta)
    i = i+1

#sort the list according to quality rank(qi) and fetch the corresponding song's#name from dictionary
i=1
rank.sort(key=itemgetter(0))
while int(splits[1]) >= i:
    if(rank[-i][0] == rank[-i-1][0]):
        rank[-i], rank[-i-1] = rank[-i-1],rank[-i]     
    print rank[-i][1][0]
    i = i + 1

