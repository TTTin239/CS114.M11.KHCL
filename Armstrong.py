a = int(input("Nhap so a: "))
temp = a
temp1 = a
kq = 0
n = 0
while a>0:
    x = a%10
    n+=1
    a=int(a/10)
    
while temp1>0:
    x= temp1%10
    kq=kq+(x**n)
    temp1=int(temp1/10) 

if kq==temp:
    print(True)
else:
    print(False)           