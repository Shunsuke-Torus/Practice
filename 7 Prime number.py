#素数判定
import math
import time

start = time.time() 
a=int(input("値を代入してa="))

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

t = time.time() - start               # 計測終了UNIX時間 -> 計算時間算出
print(f'計算にかかった時間{t}秒')        # 計算時間表示
        