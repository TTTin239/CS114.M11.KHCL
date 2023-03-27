n=int(input())
k=int(input())
p=int(input())
q=int(input())

solution=(p-1)*2+q
k1 = solution + k
k2 = solution - k
u1 = int((k1-1)/2) + 1
u2 = int((k2-1)/2) + 1
v1=int((k1+1)%2)+1
v2=int((k2+1)%2)+1	
if k1>n and k2<=0:
	print(-1)
elif k2<=0 and k1<=n:
	print(str(u1)+" "+str(v1))
elif k2>0 and k1 <n:
	if (solution-k2)>(k1-solution):
		print(str(u1)+" "+str(v1))
	else:
		print(str(u2)+" "+str(v2))
else:
	print(str(u2)+" "+str(v2))