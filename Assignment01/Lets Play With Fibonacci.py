print("let's print the first 10 fibonacci numbers:\n")
#as we know to get fibonacci series we just have to add previous 2 numbers to get the new one.
#just by following for loop with a range we can attain and fulfil the formula "Fn = Fn-1 + Fn-2"
first=0
second=1
total=0
for i in range (0,10): #we can get more numbers by just increasing the range
        print(total,end=" ")
        first=second
        second=total
        total=first+second
        