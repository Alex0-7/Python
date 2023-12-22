#Python program to check whether a number is Prime or not
def prime(n):
    if n <= 1:
        print("not prime")
        return
    for i in range (2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
        

a=int(input("Enter the no. : "))
prime(a)



