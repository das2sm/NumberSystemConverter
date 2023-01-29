# Dictionaries
BO = {'000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}  # Binary to Octal
OB = {'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}  # Octal to Binary
BH = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
# Binary to Hex
HB = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
# Hex to Binary

# Decimal to Binary
def Dec_Bin(n):
    n1 = int(n)
    binary = ''
    while n1>0:
        binary += str(n1%2)
        n1//=2
    binary = binary[::-1]
    return binary

# Decimal to Octal
def Dec_Oct(n):
    n1 = int(n)
    octal = ''
    while n1>0:
        octal += str(n1%8)
        n1//=8
    octal = octal[::-1]
    return octal

# Decimal to Hex
def Dec_Hex(n):
    dechex = ''
    n1 = int(n)
    values = {10:'A', 11:'B', 12:'C', 13:'D',14:'E', 15:'F'}
    while n1 > 0:
        if n1%16 > 9:
            dechex += values[n1%16]
        else:
            dechex += str(n1%16)
        n1//=16
    dechex = dechex[::-1]
    return dechex
 
# Binary to Decimal
def Bin_Dec(n):
    exp = len(n) - 1
    bindec = 0
    for i in n:
        bindec += int(i)*2**exp
        exp -= 1
    return bindec

# Octal to Decimal
def Oct_Dec(n):
    n = n[::-1]
    octdec = exp = 0
    for i in n:
        octdec += int(i)*8**exp
        exp += 1
    return octdec

# Hexadecimal to Decimal
def Hex_Dec(n):
    HexDec = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    n1 = n[::-1]
    exp = 0
    hexdec = 0
    for i in n1:
        if '0' <= i <= '9':
            hexdec += int(i)*16**exp
            exp += 1
        elif 'A' <= i <= 'F':
            conversion = HexDec[i]
            hexdec += conversion*16**exp
            exp += 1
        else:
            print("Invalid input.")
    return hexdec

# Binary to Octal
def Bin_Oct(n):
    binoct = ''
    finalbinoct = ''
    count = 0
    if len(n)%3 == 0:
        for i in n:
            binoct += i
            count += 1
            if count == 3:
                conversion = BO[binoct]
                finalbinoct += conversion
                binoct = ''
                count = 0
    else:
        multiplier = 3 - (len(n)%3)
        n = ('0'*multiplier) + n
        for i in n:
            binoct += i
            count += 1
            if count == 3:
                conversion = BO[binoct]
                finalbinoct += conversion
                binoct = ''
                count = 0
    
    finalbinoct2 = ''
    for i in finalbinoct:
        if i != '0':
            finalbinoct2 += i
    
    return finalbinoct2  
            
# Octal to Binary
def Oct_Bin(n):
    octbin = ''
    for i in n:
        conversion = OB[i]
        octbin += conversion
    return octbin
        

# Binary to Hexadecimal
def Bin_Hex(n):
    binhex = ''
    finalbinhex = ''
    count = 0
    if len(n)%4 == 0:
        for i in n:
            binhex += i
            count += 1
            if count == 4:
                conversion = BH[binhex]
                finalbinhex += conversion
                binhex = ''
                count = 0
    else:
        multiplier = 4 - (len(n)%4)
        n = ('0'*multiplier) + n
        for i in n:
            binhex += i
            count += 1
            if count == 4:
                conversion = BH[binhex]
                finalbinhex += conversion
                binhex = ''
                count = 0
    
    finalbinhex2 = ''
    for i in finalbinhex:
        if i != '0':
            finalbinhex2 += i
    
    return finalbinhex2

# Hexadecimal to Binary
def Hex_Bin(n):
    hexbin = ''
    for i in n:
        conversion = HB[i]
        hexbin += conversion
    return hexbin

# Octal to Hexadecimal
def Oct_Hex(n):
    n = Oct_Bin(n)
    ans = Bin_Hex(n)
    return ans

# Hexadecimal to Octal
def Hex_Oct(n):
    n = Hex_Bin(n)
    ans = Bin_Oct(n)
    return ans

def PlayAgain():
    ans = input("\nDo you want to play again? ").lower()
    return ans

again = True
invalid = False
while again:
    if not invalid:
        print('''Menu:
1) Decimal to Binary
2) Decimal to Octal
3) Decmial to Hexadecimal
4) Binary to Decimal
5) Octal to Decimal
6) Hexadecimal to Decimal
7) Binary to Octal
8) Octal to Binary
9) Binary to Hexadecimal
10) Hexadecimal to Binary
11) Octal to Hexadecimal
12) Hexadecimal to Octal''')
        
        try:
            x = int(input("\nEnter your choice: "))
            if 1 <= x <= 12:
                if x == 1:
                    n = input("Enter a decimal number: ")
                    print(f"Binary equaivalent of {n}: {Dec_Bin(n)}")
                    
                elif x == 2:
                    n = input("Enter a decimal number: ")
                    print(f"Octal equaivalent of {n}: {Dec_Oct(n)}")
                    
                elif x == 3:
                    n = input("Enter a decimal number: ")
                    print(f"Hexadecimal equaivalent of {n}: {Dec_Hex(n)}")
                    
                elif x == 4:
                    n = input("Enter a binary number: ")
                    print(f"Decimal equaivalent of {n}: {Bin_Dec(n)}")
                    
                elif x == 5:
                    n = input("Enter an octal number: ")
                    print(f"Decimal equaivalent of {n}: {Oct_Dec(n)}")
                
                elif x == 6:
                    n = input("Enter a hexadecimal: ")
                    print(f"Decimal equaivalent of {n}: {Hex_Dec(n)}")
                    
                elif x == 7:
                    n = input("Enter a binary number: ")
                    print(f"Octal equaivalent of {n}: {Bin_Oct(n)}")
                
                elif x == 8:
                    n = input("Enter an octal number: ")
                    print(f"Binary equaivalent of {n}: {Oct_Bin(n)}")
                
                elif x == 9:
                    n = input("Enter a binary number: ")
                    print(f"Hexadecimal equaivalent of {n}: {Bin_Hex(n)}")
                
                elif x == 10:
                    n = input("Enter a hexadecimal: ")
                    print(f"Binary equaivalent of {n}: {Hex_Bin(n)}")
                
                elif x == 11:
                    n = input("Enter an Octal number: ")
                    print(f"Hexadecimal equaivalent of {n}: {Oct_Hex(n)}")
                
                elif x == 12:
                    n = input("Enter a hexadecimal: ")
                    print(f"Octal equaivalent of {n}: {Hex_Oct(n)}")
                
                invalid = True
                
            else:
                print("Invalid input.\n")
                invalid = False
                
            
        
        except ValueError:
            print("Invalid input.\n")
            invalid = False
            

    elif invalid:
        ans = PlayAgain()
        if ans.startswith('n'):
            print("Program shutting down.")
            again = False
        
        elif ans.startswith('y'):
            invalid = False
            continue
        
        else:
            print("Invalid input.\n") 
            invalid = True


