def decimaltobinary(num):   
    if num < 0:
        print("None")
    elif num == 0:
        print("0000")
    
    binary = 0
    placement = 1

    while num > 0:
        remainder = num % 2
        num //= 2
        binary += remainder * placement
        placement *= 10
        

    return binary

num = int(input("What number do you want to convert?"))
print(decimaltobinary(num))