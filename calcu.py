while True:
    num1 = int(input('type 1st number: '))
    num2 = int(input('type 2nd number: '))
    num3 = (input('choose one of /,*,+,-:  '))

    if num3 == '+':
        print(num1+num2)
        break
    elif num3 == '-':
        print(num1-num2)
        break
    elif num3== '*':
        print(num1*num2)
        break
    elif num2 == 0 and num3 == '/' :
        print('you can not devide to 0')
        continue
    else: print(num1/num2)
    break
