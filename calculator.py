# Python code for a 2 input calculator
o=input("Start?('y/n')")
if o=="y":
    for i in range (0,1000):
        num1=int(input("Enter the first no: "))
        num2=int(input("Enter the second no: "))
        print("Enter the operation\nadd(+)\nsub(-)\nmul(*)\ndivide(/)\npower(**):")
        opr=input()
        if opr=="+":
            result=print("addition:",num1+num2)
        elif opr=="-":
            result=print("subtraction:",num1-num2)
        elif opr=="*":
            result=print("multiplication:",num1*num2)
        elif opr=="/":
            result=print("division:",num1/num2)
        elif opr=="**":
            result=print("power:",num1**num2)
        break
else:
    print("------")


    

