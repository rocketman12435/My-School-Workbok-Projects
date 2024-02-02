bingonums = []
bingocalls=[]
repeat = True
while repeat == True:
    bingonum = input("Please enter the bingo number: ")
    if int(bingonum)>90:
        print("The bingo number needs to be less than or equal to 90!")
        bingonums.append(bingonum)
    try:
        int(bingonum)
        bingonum = int(bingonum)
    except:
        print("Please enter a valid bingo number")
    bingocall = input("Please enter the associated bingo call for this number: ")
    bingocalls.append(bingocall)
bingonums.sort()
