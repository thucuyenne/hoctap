a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
s=int(input('S='))
d='Tien dien'
if s<=100:
    d=s*a
elif 101<=s<=150:
    d=a*100+b*(s-100)
elif s>=151:
    d=100*a+b*50+c*(s-150)
print('Phai tra=',d)
    