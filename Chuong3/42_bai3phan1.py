x=float(input('x='))
y=int(input('y='))
ch=input('Phep toan:')
if ch=='+':
    print('x',ch,'y=',x+y,sep='')
elif ch=='-':
    print(x,ch,y,'=',round((x-y),1),sep='')
elif ch=='*':
    print(x,ch,y,'=',round((x*y),1),sep='')
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        print(x,ch,y,'=',round((x/y),1),sep='')
else:
    print('Khong hop le')
