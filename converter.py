def decimaltobinary(num):   
    if num == 0:
        print("0000")
    elif num == 1:
        print("0001")
    elif num == 2:
        print("0010")    
    elif num == 3:
        print("0011")    
    elif num == 4:
        print("0100")    
    elif num == 5:
        print("0101")    
    elif num == 6:
        print("0110")    
    elif num == 7:
        print("0111")    
    elif num == 8:
        print("1000")    
    elif num == 9:
        print("1001")    
    elif num == 10:
        print("1010")    
    elif num == 11:
        print("1011")    
    elif num == 12:
        print("1100")    
    elif num == 13:
        print("1101")    
    elif num == 14:
        print("1110")    
    elif num == 15:
        print("1111")    
    elif num > 15:
        print("N/A")

num = int(input("What number between 0 - 15 do you want to convert?"))
print(decimaltobinary(num))

