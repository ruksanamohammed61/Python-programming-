m=int(input("enter starting range:"))
n=int(input("enter ending range:"))
from math import*
f=0
for i in range(n,n+1):
	for j in range(2,int(sqrt(i)+1)):
		if i%j==0:
			f=1
			break
			
	if f==0:
		print(i)	
