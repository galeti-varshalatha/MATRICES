#---------linear algebraic operations  on matrices------------
import numpy as np
a=np.array(input("enter matrix;"));
b=np.linalg.inv(a)
d=np.array(b,dtype=complex)
e=np.trace(a)
f=np.transpose(a)
c=np.linalg.det(a)
r=np.linalg.matrix_rank(a)
l=np.linalg.eig(a)
print a
print "inverse of matrix a in integer form\n",b
print"inverse of matrix a in complex form\n",d
print("trace of matrix a",e)
print("transpose of matrix a ",f)
print ("determinant of matrix a",c)
print ("rank of matrix a",r)
print ("eigen values of matrix a\n",l)
#-------------arithmetic operations on matrices---------
a1=np.array(input("enter the matrix 1="))
a2=np.array(input("enter the matrix 2="))
b1=np.add(a1,a2)
c1=np.subtract(a1,a2)
d1=np.divide(a1,a2)
e1=a1.dot(a2)
print ("addition of two matrices:\n",b1)
print ("subtraction of two matrices:\n",c1)
print ("division of two matrices:\n",d1)
print ("multiplication of two matrices:\n",e1)



