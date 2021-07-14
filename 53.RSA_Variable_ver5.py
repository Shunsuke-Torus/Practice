
import sympy

def main():   
    n,e,p,q,L = rsa()
    
    while(1):#bit,p,q,L,e
        try:
            mode = (int(input("公開鍵:1,秘密鍵:2,暗号化:3,復号化:4,終了:5 \n input:")))
            
            if mode == 1:
                
                mode1(n,e,p,q,L)
                
            elif mode ==2:
                
                mode2(n,e,p,q,L)
                
            elif mode ==3:
                
                P,C = mode3(n,e,p,q,L)
                            
            elif mode ==4:
                
                C,P = mode4(n,e,p,q,L,C) #some is not useed 
                    
            elif mode ==5:
                break
            else:
                raise ValueError
                
        except ValueError:
             print('入力値が不正です') 
             

def rsa():
    
    print("RSA")
    p_judge = int(input("pを持っているなら入力:p,持っていない:0 \n p:"))
    q_judge = int(input("qを持っているなら入力:q,持っていない:0 \n q:"))
    e_judge = int(input("eを持っているなら入力:e,持っていない:0 \n e:"))
    if(p_judge==0):
        p = sympy.randprime(pow(10,299),pow(10,300))#sympy.randprime(a,b)a以上b未満の素数を返す。未満だったので300と書いてもok
    else:
        p = p_judge
        
    if(q_judge==0):
        q = sympy.randprime(pow(10,299),pow(10,300))
    else:
        q = q_judge
        
    while(p==q):
        p = sympy.randprime(pow(10,299),pow(10,300))
    #n
    n = p*q
    
    #L
    L = int(sympy.lcm(p-1,q-1))
    
    #e
    max_num =max(p,q) 
    
    if(e_judge==0):
        while(1):
            e = sympy.randprime(max_num,L)
            if sympy.gcd(max_num,L) and max_num < e < L:
                break
    else:
        e = e_judge
    return n,e,p,q,L 
      
def mode1(n,e,p,q,L):
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")
    
def mode2(n,e,p,q,L):
    d = secret_key(e,L)
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")
    print(F"秘密鍵p:\n{p}\n秘密鍵q:\n{q}\n秘密鍵L:\n{L}\n秘密鍵d:\n{d}")

def mode3(n,e,p,q,L):
    #P　平文
    P = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
    P = char_to_int(P)
    C = encrypt(P,e,n)
    C = int_to_char(C)
    print("暗号文:",C)
    return P,C
    
def mode4(n,e,p,q,L,C):
    d = secret_key(e,L)
    mode_cryptogram = int(input("以前の暗号を利用するなら:0を入力してください。以外なら:1 \n C:"))
    if mode_cryptogram==0:
        C = char_to_int(C)
        P = dencrypt(C,d,n)
        P = int_to_char(P)
        print("P平文:",P)
    elif mode_cryptogram==1:
        C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
        C = char_to_int(C)
        P = dencrypt(C,d,n)
        P = int_to_char(P)
        print("\n P平文:",P)    
        
    return C,P

def secret_key(e,L):#受信者
    x,y,t = sympy.gcdex(e,L) 
    #d
    d = int(x) % L
    return d

def encrypt(P,e,n):#暗号化
    C = pow(P,e,n)
    return C

def dencrypt(C,d,n):#復号化
    P = pow(C,d,n)
    return P
    
     
def char_to_int(P_C: str)->int:

    P_C_list = list(P_C)#1文字ずつ格納
    P_C_size = len(P_C_list)
    total = 0
    num_list = []
    for i in range(0,P_C_size):
        num_list.append(ord(P_C_list[i])-32)
    num_list.reverse()
    
    num_list_size = len(num_list)#OZ　ありがとう　L145とL149の書き方を統一したよ7/5
    
    for i in range(0,num_list_size):
        total += num_list[i]*pow(95,i)#文字　数字　etc 95種類
    return total
    
def int_to_char(P_C_int: int) ->chr: #数字から文字 N=95
    #ユークリッドの互除法　数字を割って最小正剰余で表示
    qlist = []#商の保存先 quotient
    rlist = []#余り remainder
    while(P_C_int>=95):
        q,r = divmod(P_C_int,95)
        #q = P_C_int // 95
        #r = P_C_int % 95
        qlist.append(q)#商と余りを式の番号ごとに保存
        rlist.append(r)
        P_C_int = q
    if P_C_int // 95 < 95:#最後の追加の処理は上ではされない設計のため
        r = P_C_int % 95
        rlist.append(r)  
        
    rlist.reverse()#反転して1の位から入れる。
    
    char_list = []#数字を文字にする
    for i in range (0,len(rlist)):
        char_list.append(chr(rlist[i]+32))#+32で元の文字に戻す。特殊文字を避けるため
    P_C_char = "".join(char_list)#"",""を結合する
    
    return P_C_char


if __name__ == "__main__":
    main()
