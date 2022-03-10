# Write to enter any number and print it's prime or not
num=int(input("enter number:"))
if num > 1:
    for i in range(2,num):
        if(num % i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is  a prime number")
else:
    print(num,"is not a prime number")
