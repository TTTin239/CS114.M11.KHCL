n=int(input("Nhap vao so tu nhien: "))
Tong=0
for i in range(1,n):
    if n % i == 0:
        Tong+=i
     
print("Tong cac uoc so: ",Tong)     