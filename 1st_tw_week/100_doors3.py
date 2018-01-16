def MakeDors():
    index = 1
    while index < 101:
       dors.append(1)
       index+=1
def oc(step):
   if dors[step] == 1:
       dors[step] = 0
   else:
       dors[step] = 1
def times(x):
    i=x-1
    while i<=99:
       oc(i)
       i=i+x
dors = []
MakeDors()
t=1
while t<=100:
   times(t)
   t=t+1
opendoors = []
for i, j in enumerate(dors):
   if j == 0:
       opendoors.append(i+1)
print (opendoors)
print(len(dors))