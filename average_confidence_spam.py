fname=input('enter a file name: ')
xfile=open(fname)
count=0
total=0
total=float(total)
count=float(count)
for line in xfile:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        single=len(line[19:])
        single=float(single)
        total=total+single
ave=total/count
ave=float(ave)
print('Average spam confidence:',ave)
