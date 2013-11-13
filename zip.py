import sys
inp = sys.stdin.readline()
splits = []
songlist = []
i = 0

#total records to extract
results = inp.split()[1]

#calculate rank using zipf's law
#store rank and meta data in a list of dictionaries
i = 1
for line in sys.stdin:
    splits = line.split()
    songlist.append({'name' : splits[1], 'rank' : long(splits[0])*i}) 
    i = i+1

#sort based on rank
songlist.sort(key=lambda p:p['rank'],reverse=True)

i = 0
while int(results) > i:
    print songlist[i]['name']
    i = i + 1
