import sys
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
#for i in range(9):
#    print splits[i]

i = 1
while i <= int(splits[0]):
    testval = int(splits[i*2])
    ref = int(splits[2])/i
    q = float(testval)/float(ref)
    rank.append(q)
    songs[q] = splits[(i*2)+1]
    i = i+1

#sort the list according to quality rank(qi) and fetch the corresponding song's#name from dictionary
i=1
rank.sort(key=int)
while int(splits[1]) >= i:
    print songs.get(rank[-i])
    i = i + 1

