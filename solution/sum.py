# was to enter any number and print of sum of digit
a=int(input("enter any number"))
sum=0
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of digits of {}".format(sum))
