#GCD
a=int(input("a="))
b=int(input("b="))
r=a     

while (r!=0):
    q =a//b
    r =a%b
    print(a,"=",q,"X",b,"+",r)
    a=b
    b=r
print("GCD=",a)