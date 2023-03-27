from decimal import*
import decimal
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
import math
def HoanVi(a, b):
    temp=a
    a=b
    b=temp
    return a,b
if b>a:
    a,b=HoanVi(a,b)
if c>a:
    c,a=HoanVi(c, a)
if c>b:
    c, b=HoanVi(c, b)

if (a+b)>c and (a+c)>b and (b+c)>a:
    d=(a+b+c)/2
    s=math.sqrt(d*(d-a)*(d-b)*(d-c))
    s=round(s,2)
    if s%1==0:
        s=int(s)
    if a==b and b==c:
        print("Tam giac deu, dien tich = "+str(s))
    elif b==c or a==b :
        print("Tam giac can, dien tich = "+str(s))
    elif a**2==(b**2+c**2):
        print("Tam giac vuong, dien tich = "+str(s))
    else:
        print("Tam giac thuong, dien tich = "+str(s))
else:
    print("Khong phai la tam giac.")                         