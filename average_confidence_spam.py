#this code calculates the average spam confidence in file 'mbox-short.txt'
fname=input('enter a file name: ')
xfile=open(fname)
count=0
total=0
total=float(total)
count=float(count)
for line in xfile:
    if line.startswith('X-DSPAM-Confidence:'): #extracting the value of spam confidences
        count=count+1 #adding up the quantity of values
        single=len(line[19:]) #exact position of wanted number
        single=float(single)
        total=total+single
ave=total/count #calculate
ave=float(ave)
print('Average spam confidence:',ave)
