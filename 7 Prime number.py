#prime-number
import math
import time

start = time.time() 
a=int(input("substitute a="))

def isprime(a):
    if a<=1:
        return False

    if a==2:
        return True
    
    if a%2==0:
        return False
    for i in range(3,math.ceil(math.sqrt(a))+1,2):
        if a%i==0:
            return False
    return True
print(isprime(a))

t = time.time() - start             
print("The time it takes to complete the calculation is {t}sec")        
        
        
