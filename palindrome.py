n=int(input("enter n value:"))
k=n
s=0
while n>0:
	s=s*10+n%10
	n=n//10
	print("reverse is:",s)
	if k==s:
		print("palindrome")
		
	else:
				print("not palindrome")
			
			