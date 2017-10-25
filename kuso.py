import time
f=open("kusotable.txt",'w')
signals=[]
numbers=[]
formulation=[]
answer=[]
start=time.clock()
def getformulation(n,temp,statue):
	if n==0:
		temp+=['s' for i in range(statue)]
		global formulation
		formulation.append(temp)
		return
	for i in range(1,statue+1):
		getformulation(n,temp+['s' for j in range(i)],statue-i)
	temp.append('n')
	getformulation(n-1,temp,statue+1)
	return

def allnums(a,b,c,temp):
	if a==0 and b==0 and c==0:
		global numbers
		numbers.append(temp)
		return
	if a:
		allnums(a-1,b,c,temp+['1'])
	if b:
		allnums(a,b-1,c,temp+['4'])
	if c:
		allnums(a,b,c-1,temp+['5'])
		

def getsignals(temp,n):
	if n==0:
		global signals
		signals.append(temp)
		return
	getsignals(temp+['+'],n-1)
	getsignals(temp+['-'],n-1)
	getsignals(temp+['*'],n-1)
	getsignals(temp+['/'],n-1)
	getsignals(temp+['_'],n-1)
	
def calculatep(formulat,number,signal):
	stack=[]
	j,k=0,0
	flag=0
	tempstr=[]
	for i in formulat:
		if i=='n':
			stack.append(number[j])
			tempstr.append(number[j])
			j+=1	
		else:
			sa=tempstr.pop()
			sb=tempstr.pop()
			if signal[k]!='_':
				tempstr.append('('+sb+signal[k]+sa+')')
			else:
				tempstr.append(sb+' '+sa)
			b=stack.pop()
			a=stack.pop()
			if signal[k]=='+':
				stack.append(int(a)+int(b))
			elif signal[k]=='-':
				stack.append(int(a)-int(b))
			elif signal[k]=='*':
				stack.append(int(a)*int(b))
			elif signal[k]=='/':
				if int(b)==0:
					return
				else:
					stack.append(int(a)//int(b))
			else:
				if sa[0]=='(' or sb[0]=='(':
					return
				else:
					stack.append(int(str(a)+str(b)))
			k+=1
	global answer
	temp=stack.pop()
	if temp in answer:
		return
	else:
		answer.append(temp)
		sa=tempstr.pop()
		sa=sa[1:-1] if sa[0]=='(' else sa
		ans=str(temp)
		blank="".join([' ' for i in range(12-2*len(ans))])
		sb=blank
		for i in ans:
			sb+=i+' '
		f.write(sb+"= "+sa+'\n')

getformulation(5,['n'],0)
getsignals([],5)
allnums(3,2,1,[])
for i in formulation:
	for j in signals:
		for k in numbers:
			calculatep(i,k,j)
answer.sort()
f.write("possible answers:\n")
for i in answer:
	f.write(str(i)+'\n')
f.close()
elapsed=(time.clock()-start)
print "cost: "+str(elapsed)+"   YADAZE!"