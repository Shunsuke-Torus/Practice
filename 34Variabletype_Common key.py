# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:35:07 2021

@author: Shun
"""
import sympy as sp

def insert():
    
    print("P,C,A,A^-1を持っていますか。持っている:1持っていない:0")
    function = int(input("function:"))
    
    if  function==1:
        row = int(input("行row="))
        column = int(input("列column="))
        a = row * column

        A = sp.Matrix(row,column,range(a))

        print("挿入してください　順番が異なるので注意してください")

        print(A)
        for i in range (row):#012
            for j in range (column):#01
                print("Now row=",i,"\t","Now column=",j)
                A[i,j]=int(input("順番に注意_数字="))
        return A
    
    else:#他は考慮しない
        return 
                        
print("平文P、暗号文C、暗号化鍵A、復号化鍵A^-1の中であるものを「1」と代入してください。")
mod = int(input("mod="))
P = insert()
C = insert()
A = insert()
A_inverse = insert()

if C!=None and P!=None:
    P_inv=P.inv_mod(mod)
    print("A×",P,"≡",C,"(mod",mod,")\n")
    print("A≡",C,"×",P_inv,"\n")
    
    print("暗号化鍵を作れました。encryption-key made")
    A=(C*P_inv)%mod
    print("A≡",A,"(mod",mod,")\n")
    
    print("復号化鍵を作れました。decryption-key made")
    A_inverse=A.inv_mod(mod)
    print("A^-1≡",A_inverse,"(mod",mod,")\n")
    
elif C!=None and A!=None:
    print("復号化鍵を作れました。decryption-key made")
    A_inverse=A.inv_mod(mod)
    print("A^-1≡",A_inverse,"(mod",mod,")\n")
    print("A^-1≡",A_inverse,"×",C,"\n")
    
    P=(A_inverse*C)%mod
    print("復号化を完了しました")
    print("P≡",P)
    
elif C!=None and A_inverse!=None:
    print("暗号化鍵を作れました。encryption-key made")#特殊
    A = A_inverse.inv_mod(mod)
    print(A)
    print("A_inverse=",A*A_inverse)
    
    P=(A_inverse*C)%mod
    print("復号化を完了しました")
    print("P≡",P)
    
elif P!=None and A!=None:
    print("復号化鍵を作成成功　decryption-key made")
    A_inverse=A.inv_mod(mod)
    print("A^-1≡",A_inverse,"(mod",mod,")\n")
    print("A^-1≡",A_inverse,"×",C,"\n")
    
    print("暗号文を作成成功")
    C = (A*P)%mod
    print("C≡",C,"(mod",mod,")\n")
    
elif P!=None and A_inverse!=None:
    print("暗号化鍵を作れました。encryption-key made")#特殊
    A = A_inverse.inv_mod(mod)
    print(A)
    print("A_inverse=",A*A_inverse)
    
    print("暗号文を作成成功")
    C = (A*P)%mod
    print("C≡",C,"(mod",mod,")\n")
    

   

