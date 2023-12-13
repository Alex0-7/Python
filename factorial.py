#Write a Python program to find the factorial of a number using while loop
def fact(n):
    num=1
    while n>=1 :
        num= n * num
        n=n-1
    return num
a=int(input("enter the number to factorise: "))
print(fact(a))
