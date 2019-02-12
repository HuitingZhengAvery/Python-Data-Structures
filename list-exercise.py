#this python code extracts all words in a poem (which is romeo.txt here) and puts them in a list

fname=input('enter file name: ')
xfile=open(fname)
x=list()
for line in xfile:
    line=line.rstrip() #eliminate new lines
    word=line.split()  #split by spaces
    for t in word:
        if t not in x:
            x.append(t) #adding words into the empty list
x.sort()
print(x)
