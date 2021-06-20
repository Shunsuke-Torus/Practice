
#渡された公開鍵から暗号文を作成

n = int(input("n="))
e = int(input("e="))
P = int(input("P平文="))
N = int(input("N（法）="))
O = int(input("O 元々の進数、通常10進数="))


def change(P,N):#N進数への変換
    
    n = len(str(abs(P)))#size
    n = int(n)
    print("n=",n)
    l_list =[] 
    box=0
    #人間的
    for i in range(n-1,0,-1):#分割したい　それぞれの位で 
        box = P//(O**i)
        P -=  box*(O**i)
        print("P=",P)
        l_list.append(box)#insert(abs(n-(i+1)),box)
        if i==1:
            l_list.append(P)
            break
    #順番を逆転させることによって1の位から計算
    l_list.reverse()
    
    for i in range(0,n,1):
        box = l_list[i]
        if i==0:
            P=l_list[i]
        else:
            P +=  box*(N**i)
        
    return P #N進数へと変換された数字

def calculation(huge_amount,N):
    qlist = []#商の保存先
    rlist = []#余り
    while(huge_amount>=N):
        q = huge_amount//N
        r = huge_amount%N
        qlist.append(q)#商と余りを式の番号ごとに保存
        rlist.append(r)
        huge_amount=q
    if huge_amount//N < N:
        r = huge_amount%N
        rlist.append(r)    
    rlist.reverse()

if __name__ == "__main__":    
    P = change(P,N)

    print("C≡",P,"^",e,"(mod",n,")")

    huge_amount = P**e % n
    print(huge_amount)

    C = calculation(huge_amount,N)
    print("暗号化番号:",C)






