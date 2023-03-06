a=float(input('Tieu thu='))
b='Don gia'
if 1<=a<=100:
    b=a*550
elif 101<=a<=150:
   b=550*100+750*(a-100)
elif 151<=a<=200:
    b=550*100+750*50+950*(a-150)
elif a>=201:
    b=550*100+750*50+950*50+1350*(a-200)
print('Phai tra',b+b*float(10/100))