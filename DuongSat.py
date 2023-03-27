k,n=input().split()
k=int(k)
n=int(n)
if n>k:
    if int((n/k))%2==0:
        print(int(n%k))
    else:
        print(int(k-(n%k)))
else:
    print(int(n))            