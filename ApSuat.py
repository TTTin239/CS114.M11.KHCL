from decimal import*
import decimal
n = float(input("Nhap vao so n: "))
s = n*0.453592/(2.54**2)
getcontext().prec = 6
s= Decimal(s)
print(s.normalize())