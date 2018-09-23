# IT WAS PERFORMING ADD,SUB,MUL AND DIVISION OPERATIONS

def calculator(num1,num2):
    operation = input("enter the which operation you want \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n ")
    if operation == 1:
        a = num1 + num2
        print(a)
    elif operation == 2:
        b = num1 - num2
        print(b)
    elif operation == 3:
        c = num1 * num2
        print(c)
    elif operation == 4:
        d = num1 / num2
        print(d)
    else:
        print('please try again')
number1 = input("enter the number 1 \n")
number2 = input("enter the number 2 \n")
calculator(number1,number2)
