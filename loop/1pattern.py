i=1
while i<=10:
    if i==1:
        print(' '*(10-1)+'*')
    elif i==10:
        print('*'*(2*i-1))

    else:
        print(" "*(10-i)+'*'+' '*(2*i-3) +'*')

    i=i+1     