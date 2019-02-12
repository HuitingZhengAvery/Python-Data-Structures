fname=input('enter a file name: ')
xfile=open(fname)
lst=list()
for line in xfile:
    if not line.startswith('From '):
        continue
    y=line.split()
    y=y[5]
    lst.append(y)
counts=dict()
final=list()
for time in lst:
    time=time[:2]
    final.append(time)
for z in final:
    counts[z]=counts.get(z,0)+1
llst=list()
for hour,val in counts.items():
    newtup=(hour,val)
    llst.append(newtup)
llst=sorted(llst)
for a,b in llst:
    print(a,b)
