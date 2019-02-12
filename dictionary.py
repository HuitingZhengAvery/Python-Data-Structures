fname=input('enter a file name: ')
xfile=open(fname)
t=list()
counts=dict()
for line in xfile:
    if not line.startswith('From '):
        continue
    y=line.split()
    name=y[1]
    t.append(name)
for person in t:
    counts[person]=counts.get(person,0)+1
bigperson=None
bigcount=None
for person,count in counts.items():
    if bigcount is None or count>bigcount:
        bigperson=person
        bigcount=count
print(bigperson,bigcount)
