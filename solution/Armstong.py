#was to enter Armstong number
num=int(input("Enter a number:"))
sum=0
tem=num
while tem>0:
    digit=tem%10
    sum+=digit**3
    tem//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstong number")
