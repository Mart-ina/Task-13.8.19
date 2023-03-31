coupon=int(input('Какое количество билетов:'))
rate=0
for i in range(coupon):
     age = int(input('Сколько вам лет:'))
     if 0 < age < 18:
         rate = rate+0
     elif 18 <= age < 24:
         rate = rate+990
     else:
         rate = rate+1390
if coupon > 3:
    rate = rate * 0.9
print('Сумма %d' %(rate))