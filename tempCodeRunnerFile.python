while (True):
    kolich = int(input('Введите количество операций: '))
    i = 0
    chislo1 = float(input('Введите первое число: '))
    chislo2 = float(input('Введите второе число: '))
    while i != kolich:
        print('')
        print('Сложение: + \nВычитание: - \nУмножение: * \nДеление: /')
        print('')  
        oper = input('Выберите операцию: ') 
        if(oper == '+'):
            chislo1= chislo1+chislo2
            print('Ответ: ' , chislo1)
            i+=1
            if i==kolich:
                i=0
                break
            chislo2 = float(input('Введите  число: '))   
        elif(oper == '-'): 
            chislo1= chislo1-chislo2
            print('Ответ: ' , chislo1)
            i+=1
            if i==kolich:
                i=0
                break
            chislo2 = float(input('Введите  число: '))
        elif(oper == '*'): 
            chislo1= chislo1*chislo2
            print('Ответ: ' , chislo1)
            i+=1
            if i==kolich:
                i=0
                break
            chislo2 = float(input('Введите  число: '))  
        elif(oper == '/'):  
            if(chislo2==0):
                print('Делить на ноль нельзя')  
                chislo2 = float(input('Введите  число: '))  
                if (chislo2 !=0):
                    chislo1= chislo1/chislo2
                    print('Ответ: ' , chislo1)
                    i+=1
                    if i==kolich:
                        i=0
                        break
                chislo2 = float(input('Введите  число: '))
            elif (chislo2!=0):       
                chislo1= chislo1/chislo2
                print('Ответ: ' , chislo1)
                i+=1
                if i==kolich:
                    i=0
                    break
                chislo2 = float(input('Введите  число: '))         