fname=input("enter file name:")
m=w=c=0
try:
	f=open(fname,"r")
	for i in f.readlines():
		m=m+1
		for j in i.split():
			w=w+1
			for k in j:
				c=c+1
				print("lines count:",m)
				print("words count:",w)
				print("characters count:",c)
				f.close()
except FileNotFoundError as e:
	print(e)