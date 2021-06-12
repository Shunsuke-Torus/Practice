#暗号化鍵及び復号化鍵+復号化　2×2　と　2×2　と　2×3のみ対応
#2021/6/21
import sympy
import sys

sympy.init_printing()
sympy.var("a,b,c,d,e,f,g,h,i,j,k,l,m,n")

print("鍵を求める:0,復号化を求める:1")
need=int(input("need="))
try:
    print("平文の行列を入力してください。上下の順番に気を付けてください")
    print("[a][c]")
    print("[b][d] (mod)")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    d = int(input("d="))
    mod = int(input("mod="))

    P = sympy.Matrix([ 
        [a,c],
        [b,d]
    ])

    print("次に暗号文の行列を入力してください。上下の順番に気を付けてください")
    print("[e][g]")
    print("[f][h]")
    e = int(input("e="))
    f = int(input("f="))
    g = int(input("g="))
    h = int(input("h="))

    B = sympy.Matrix([
        [e,g],
        [f,h]
    ])
except ValueError:
    print("Please try again")
    sys.exit()

P_inv=P.inv_mod(mod)
print("A×",P,"≡",B,"(mod",mod,")\n")
print("平文の^-1をかけて逆行列にして両辺に掛ける。左辺を単位行列にする\n")
print("逆行列P^-1≡",P_inv,"(mod",mod,")\n")
print("A×",P,"×",P_inv,"≡",B,"×",P_inv,"(mod",mod,")\n")
print("A≡",B,"×",P_inv,"\n")

P_key=(B*P_inv)
print("mod前の暗号化鍵A≡",P_key)

P_key=(B*P_inv)%mod
print("暗号化鍵を作れました。encryption-key made")
print("A≡",P_key,"(mod",mod,")\n")

P_decryption_key=P_key.inv_mod(mod)
print("復号化鍵を作れました。decryption-key made")
print("A^-1≡",P_decryption_key,"(mod",mod,")\n")

if (need==1):
    try:
        print("暗号文を復号化するよ。順番に注意")
        print("[i][k][m]")
        print("[j][l][n]\n")
        i = int(input("i="))
        j = int(input("j="))
        k = int(input("k="))
        l = int(input("l="))
        m = int(input("m="))
        n = int(input("n="))
    
        C = sympy.Matrix([ 
            [i,k,m],
            [j,l,n]
        ])#2×2でも余っている部分は0を代入
    except ValueError:
        print("Please try again")
        sys.exit()  
    
    print("P≡A^-1≡",P_decryption_key,"×",C,"\n")
    P_ans=P_decryption_key*C
    print(P_ans)
    P_ans=P_ans%mod
    print("復号化完了")
    print("P≡",P_ans)
    

