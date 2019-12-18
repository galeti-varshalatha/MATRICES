import numpy as np
a=input("enter the array a")
b=input("enter the array b")
print "the elements in array a \n",a
d=np.append(a,b)
print "elements of array a",d
for i in range(0,len(b)):
	if(b[i]>=0):
		a.append(b[i])
print a
