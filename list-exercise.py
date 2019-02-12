fname=input('enter file name: ')
xfile=open(fname)
x=list()
for line in xfile:
    line=line.rstrip()
    word=line.split()
    for t in word:
        if t not in x:
            x.append(t)
x.sort()
print(x)
