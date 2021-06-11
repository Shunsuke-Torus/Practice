#逆行列の求め方

import numpy as np

print("[a][b]")
print("[c][d] (mod)")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
mod = int(input("mod="))

A = np.array([[a, b], [c, d]])
print(A)
check = A

#scalar = np.linalg.det(A)#https://qiita.com/kyoro1/items/9ff500db0d519bd2a6f5
scalar =a*d-b*c
print(scalar)

scalar = scalar % mod
print(scalar)

print(scalar,"x","≡","1","(mod",mod,")")

qlist = []#商とあまりの保存先
rlist = []
j=scalar
l=scalar
k=mod
i=0
while (l>=1):
    q =j//k
    l =j%k
    qlist.append(q)#商と余りを式の番号ごとに保存
    rlist.append(l)
    print("(",i,")",l,"=",j,"-",q,"*",k)
    j=k
    k=l
    i +=1
else:
    print("ループが終了しました")
print("GCD=",j)

def calculation(start,stop):
    ans = []                
    min = float("inf")     
    r = range(start,stop)   
    for x in r:                 
        for y in r:           
            if scalar*x+mod*y==1:
                if x*x+y*y< min:              
                    if len(ans)!=0: ans.pop()       
                    ans.append([x,y])              
                    min = x*x+y*y                  
                elif x*x+y*y==min:                         
                    ans.append([x,y])                              
    return ans

ans1=calculation(-100,100) 
if ans1==[]:
    ans1=calculation(-1000,1000)  
if ans1==[]:
    ans1=calculation(-10000,10000)

Aminusone= ans1[0][0] % mod
print("x","≡",Aminusone,"(mod",mod,")")

print(A)
e = a
a = d
d = e
A = np.array([[a, -b], [-c, d]])
print("A^-1≡",Aminusone,"×")#Aminusone mean A^-1
print(A)

result = Aminusone * A

print(result)
result = result % mod 

print(result,"(mod",mod,")")

check = np.dot(check,result)
print(check)
check = check % mod
print(check,"(mod",mod,")")
