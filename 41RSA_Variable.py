# -*- coding: utf-8 -*-
"""

未完

Created on Tue Jun 22 09:46:41 2021

@author: Shun

公開鍵暗号方式
C≡P^e(mod n) 暗号化

P≡C^d(mod n)　復号化

ディジタル署名
C≡P^d(mod n) 暗号化

P≡C^e(mod n)　復号化

n=p*q

L=LCM(p-1,q-1)=p-1*q-1/gcd(p,q)

Max{p,q}<e<L and L e が互いに素な数
gcd(l,e)=1

暗号文C =平文^e mod N
平文P   =暗号文^d mod N

平文       N     d 
暗号文     N   e
公開鍵     N L e d 
秘密鍵     N L e d

"""
#from rsa import Rsa
import sympy
import sys
def main():
    
    print("RSA")
    print("持っているなら数字を入力、持っていないなら0を入力")
    str_list = ["n","e","N","d","P","p","q","L","C"]#公開　n,e 秘密 p,q,L
    num_list = [89711,3251,26,0,0,0,0,0,0]#[]あとで変更
    #for i in range (0,len(str_list)):
    #    print(str_list[i])
    #    num_list.append(int(input()))
        
    if num_list[0]==0 and num_list[5]!=0 and num_list[6]:
        num_list[0] = num_list[5]*num_list[6]
    
    elif(num_list[0]!=0 and (num_list[5]==0 and num_list[6]==0)):#nがあるがp,qどちらかがないとき　素因数分解
        factorization_box,factorization_size = prime_factorization(num_list[0])#複数の戻り値
         
        for i in range (0,factorization_size):
            if num_list[0]==factorization_box[i]*factorization_box[-(i-1)]:
                num_list[5] = factorization_box[i]
                num_list[6] = factorization_box[-(i-1)]
                #break:
        
    elif(num_list[0]!=0 and (num_list[5]==0 or num_list[6]==0)):
        if num_list[5]==0:
            num_list[6] = num_list[0]/num_list[6]#q
        else:
            num_list[5] = num_list[0]/num_list[5]#p
            
    a = int(input("暗号化:0,復号化:1,ディジタル暗号化:2,ディジタル復号化:3,miss:4/t"))
    if a==0:
        P_C_size,int_list=P_C_siz()
        print("暗号化")
        print("C≡P^e (mod n)")
        if P_C_size!=0:
            int_list.reverse()
            P = change_n_to_dec(int_list,num_list[2],P_C_size)#int_list,N,P_size
            
        C = calculate(num_list[0],P,num_list[1])#n,P,e→"C or P ≡",i,"^",j,"(mod",n,")"
        print("C:",C)
        C = change_dec_to_n(C,num_list[2])
        print("C:",C)
                
    elif a==1:
        P_C_size,int_list=P_C_siz()
        
        print("復号化")
        print("P≡C^d (mod n)")
        
        if P_C_size!=0:
            int_list.reverse()
            C = change_n_to_dec(int_list,num_list[2],P_C_size)#int_list,N,P_size
            num_list[8] = C
            
        if num_list[3]==0:#d
            num_list[3] = secret_key(num_list[0],num_list[1],num_list[5],num_list[6]) #d=secret_key(n,e,p,q)
            
        P = calculate(num_list[0],C,num_list[3])#n,C,d → n,i,j
        
        P =change_dec_to_n(P,num_list[2])#mistake
        num_list[4] = P
        print("P平文:",P)
        
    elif a==2:
        print("ディジタル暗号化")
        
        
    elif a==3:
        print("ディジタル復号化")
    else:#miss
        exit() 
        

#https://ictsr4.com/py/m0120.html
def prime_factorization(num):
    factorization = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            factorization.append(i)  
            if pow(i,2) == num:  
                continue
            factorization.append(num//i) 
#     return factorization  
    return sorted(factorization),len(factorization)

#2021/6/27ここから　secret-key make　n,p,qは完成
#secret_key(num_list[0],num_list[5],num_list[6])        
def secret_key(n,e,p,q):#n,p,q
    
    L = sympy.lcm(p-1,q-1)
    print("最小公倍数LCM:",L)
    print("ed+Ly=1")
    x,y,t = sympy.gcdex(e,L)
    d = int(x)
    d = x % L # mod = L
    print("秘密鍵鍵製作完了d:",d)
    
    return int(d)
        
def P_C_siz():
    P_C_size = int(input("P or Cのsizeは:"))
    int_list = []
    for j in range (0,P_C_size):
        int_list.append(int(input(":")))
    return P_C_size,int_list        

def calculate (n,i,j):#n,i,j
    print("C or P ≡",i,"^",j,"(mod",n,")")  
    b = i**j % n       
    return int(b)

def change_dec_to_n(amount,N):#Dec→n

    qlist = []#商の保存先
    rlist = []#余り
    while(amount>=N):
        q = amount//N
        r = amount%N
        qlist.append(q)#商と余りを式の番号ごとに保存
        rlist.append(r)
        amount=q
    if amount//N < N:
        r = amount%N
        rlist.append(r)    
    rlist.reverse()
    return rlist   

def change_n_to_dec(int_list,N,P_size):#n→Dec
    total = 0
    for j in range (0,P_size):
        o = pow(N,j)
        int_list[j]=int_list[j]*o
        total +=int_list[j]
    return total  

if __name__ == "__main__":
    main()