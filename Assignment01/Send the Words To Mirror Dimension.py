something=input("Write anything you want!\n")
length=len(something)
print("So, if we reverse what you have written.\nIt will look something like this...\n???? ???? ???? ???? ????")
for i in range(length-1,-1,-1):
    print(something[i],end="")
    #just trying to be a little creative! 