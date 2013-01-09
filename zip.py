import sys
from operator import itemgetter
inp = sys.stdin.readlines()
splits = []
rank = []
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
    meta.append(i)
    meta.append(splits[(i*2)+1])
    ranked_meta = []
    ranked_meta.append(q)
    ranked_meta.append(meta)
    rank.append(ranked_meta)
    i = i+1

rank.sort(key=itemgetter(0))
#sort the list according to quality rank(qi) and fetch the corresponding song's#name from dictionary
i=1
while int(splits[1]) >= i:
   dups = []
   for o, sublist in enumerate(rank):
       if rank[-1][0] in sublist:
           dups.append(o)
   result = min(rank[p][1][0] for p in dups)
   for o, sublist in enumerate(rank):
       if result in sublist[1]:
           print rank[o][1][1]
           del rank[o]
   i = i + 1


