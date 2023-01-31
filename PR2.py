while (True):
    year = int(input('Введите год: '))
    day = 0
    summ = 0
    #summ1 = 0
   # summ2 = 0
    #rezult = []
    if ((year % 4) == 0):
        print('Високосный год')
        while day <31:
            day += 1    
            rezult = [int(a) for a in str(day)]
            if (rezult==[3,0]):
                summ1 = sum(rezult)
                summ1 = summ + summ1
            if (rezult==[2,9]):
                summ2 = sum(rezult)
                summ2 = summ + summ2
            summ = sum(rezult) + summ
        print("Сумма цифр в году = " , summ*7+summ1*4+summ2)    
    elif ((year % 4) > 0):
        print('Невисокосный год')
        while day <31:
            day += 1    
            rezult = [int(a) for a in str(day)]
            if (rezult==[3,0]):
                summ1 = sum(rezult)
                summ1 = summ + summ1
            if (rezult==[2,8]):
                summ2 = sum(rezult)
                summ2 = summ + summ2
            summ = sum(rezult) + summ
        print("Сумма цифр в году = " , summ*7+summ1*4+summ2)    