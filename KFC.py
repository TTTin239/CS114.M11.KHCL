# from decimal import*
# import decimal
# f=float(input())
# c=(f-32)/1.8
# k=c+273.15
# getcontext().prec=6
# c=Decimal(c)
# k=Decimal(k)
# print(c.normalize(),k.normalize())
from googletrans import Translator
 
translator = Translator()
 
translated = translator.translate('tôi thích bạn', src='vi', dest='en')
 
print(translated.text)