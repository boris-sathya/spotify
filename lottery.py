from math import ceil

m = n = t = p = 0

def getInput():
    global m,n,t,p
    values = raw_input()
    splits = values.split()
    m = int(splits[0])
    n = int(splits[1])
    t = int(splits[2])
    p = int(splits[3])

def nck(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    c = 1
    for i in range(k):
	c *= (n - i)
	c = c // (i + 1)
        
    return c


getInput()
required =  int(ceil(float(p)/float(t)))
loss = 0.0

for i in range(required,p+1):
	loss += (float(nck(p, i)) * float(nck(m-p, n-i)))/float(nck(m,n))

print ("%.9f" %loss)

