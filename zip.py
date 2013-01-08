inp = raw_input()
splits = inp.split()
q = 0.0
rank = []
songs = {}
i=1

while i<=int(splits[0]):
    i = i + 1
i = 1
while i<=int(splits[0]):
    testval = int(splits[i*2])
    ref = int(splits[2])/i
    q = float(testval)/float(ref)
    rank.append(q)
    songs[q] = splits[(i*2)+1]
    i = i+1
rank.sort(key=int)
i=1
while int(splits[1]) >= i:
    print songs.get(rank[-i])
    i = i + 1
