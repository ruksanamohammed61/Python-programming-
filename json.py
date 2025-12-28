
import json
def check_complex(d):
 if isinstance(d,dict):
 for i in d.values():
 if isinstance(i,(dict,list)):
 return True
 if isinstance(i,(dict,list)) and check_complex(i):
 return True
 elif isinstance(d,list):
 for i in d:
 if isinstance(i,(dict,list)):
 return True
 if isinstance(i,(dict,list)) and check_complex(i):
 return True
 return False
d={'student':{'no':1200,'name':'raju'},
 'college':['gec',48,'gudlavalleru'],1:5}
k=json.dumps(d)
p=json.loads(k)
h=123
c=check_complex(p)
r=check_complex(h)
if c==True:
 print("it contains complex object")
else:
	print("it is not complex object")
if r==True:
 print("it contains complex object")
else:
 print("it is not complex object")