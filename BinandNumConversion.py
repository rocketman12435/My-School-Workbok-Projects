binnums = [128,64,32,16,8,4,2,1]
def binary():
    bit = 128
    ans = ""  
    numinput = int(input("Enter a base 10 number to convert to binary: "))
    if numinput.isdigit() == False:
        print("Not a base 10 number!")
        exit()
    if numinput > 255:
        print("Your number is too big!")
        exit()
    elif numinput < 0:
        print("Your number is too small!")
        exit()
    else:
        for x in range(8):
            if numinput%2==0:
                

                ans=ans+"0"
                numinput = numinput/2
                
            elif numinput%2==1:
                

                ans=ans+"1"
                numinput=numinput-1

                numinput = numinput/2

    print("The binary is:",ans[::-1])

def number():
    ans = 0
    binarynum = 128
    binary = input("Enter an 8-bit binary number to convert to a base 10 number: ")
    if binary.isdigit() == False:
        print("Not a binary number!")
        exit()
    if len(binary)>=9:
        print("This is not 8-bit binary!")
        exit()
    elif len(binary)!= 8:
        print("Please enter a number with 8 binary digits (for example 1 in base 10 would be 00000001 in binary).")
        exit()
    printnum = [128,"   ",64,"   ",32,"   ",16,"   ",8,"    ",4,"     ",2,"     ",1]
    printbin = [binary[0],"     ",binary[1],"    ",binary[2],"    ",binary[3],"    ",binary[4],"    ",binary[5],"     ",binary[6],"     ",binary[7]]
    for x in range(len(binary)):
        
        binaryx = int(binary[x])
        #print(binarynum,"is binary no",binaryx)
        if binaryx == 1: 
            
            ans = ans+binarynum
        elif binaryx == 0:
            ans=ans+0
        binarynum=binarynum/2
    print(*printnum)
    print(*printbin)
    print("The answer in base 10 is:",int(ans))
repeat = True
while repeat == True:
    mode = input("Do you want to enter binary, or base 10? Please press 1 for binary and 2 for base 10: ")
    if mode == "1":
        repeat = False
        print("----------------BINARY----------------\n")
        binary()
        
    elif mode == "2":
        repeat = False
        print("----------------BASE 10----------------\n")
        number()
        
    else:
        repeat = True
        print("Please enter the correct choice.")