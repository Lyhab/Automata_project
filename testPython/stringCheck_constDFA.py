x=int(input("Enter the number of states: "))
s=[input("Enter the state: ")for i in range(0, x)]
y=int(input("Enter the number of keys: "))
t=[input("Enter the keys: ")for j in range(0, y)]
last=input("final state.................")
k=[0 for i in range(len(s))]
for i in range(len(s)):
    k[i]=[0 for j in range(len(t))]
    for j in range(len(t)):
        k[i][j]=input('from ' + s[i] + ' if ' + t[j] + ' go.......:')
def convert(p, q):
    li.append(k[s.index(p)][t.index(q)])
    return k[s.index(p)][t.index(q)]
while True:
    li=[]
    start=s[0]
    q=input("enter the string to check.......................")
    for i in q:
        start=convert(start, i)
    if (li[-1]==last):
        print("yes")
    else:
        print("no")