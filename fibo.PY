n = int(input("Nhap vao so tu nhien n: "))
f1=1
f2=1
f=0
if n<1 or n>30:
    print("So "+str(n)+" khong nam trong khoang [1;30].")
else:
    if n==1 and n==2:
        print(1)
    else:
        for i in range(n-2):
            f=f1+f2
            f1=f2
            f2=f
        print(f)           