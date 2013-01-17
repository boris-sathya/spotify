import sys
from operator import itemgetter
inp = sys.stdin.readlines()
splits = []
songlist = []
i = 0

#Chops Input Data into a list
while len(inp) > i:
    splits = splits + (inp[i].split())
    i = i + 1

#calculate rank using zipf's law
#store rank and  meta data in a list of dictionaries
i = 1
while i <= int(splits[0]):
    testval = int(splits[i*2])
    ref = int(splits[2])/i
    q = float(testval)/float(ref)
    meta = {}
    meta['id'] = i
    meta['name'] = splits[(i*2)+1]
    meta['rank'] = q
    songlist.append(meta)
    i = i+1

#two key sort (Rev Sort based on rank and Sort based on ID)
songlist.sort(key=itemgetter('rank'),reverse=True)
i = 0
while int(splits[1]) > i:
    print songlist[i]['name']
    i = i + 1
