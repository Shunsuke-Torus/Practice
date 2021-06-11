#ユークリッドの互除法の求め方
#1次不定方程式 ベズーの等式
import time
alist = []#商とあまりの保存先
blist = []

a=int(input("a="))     #bより大きい数字を代入
b=int(input("b="))

start1=time.time()       # 処理前の時刻

j=a
k=b
l=a
i=0
while (l>=1):
    q =j//k
    l =j%k
    alist.append(q)#商と余りを式の番号ごとに保存
    blist.append(l)
    print("(",i,")",l,"=",j,"-",q,"*",k)
    j=k
    k=l
    i +=1
else:
    print("ループが終了しました")
print("GCD=",j)

print(a,"x","+",b,"y","=",j)
if j!=1:  
    a=a/j   
    b=b/j   
    j=j/j
    print(a,"x","+",b,"y","=",j)
  
# calculation
def calculation(start,stop):#演算 ベズーの等式
    ans = []               
    min = float("inf")      # infinity
    r = range(start,stop)   
    for x in r:                   
        for y in r:           
            if a*x+b*y==1:
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
    
elapsed_time=time.time()-start1
print(ans1)
print("elapsed_time:{0}".format(elapsed_time)+"[sec]")

#improvement: calculation
#Citation site: http://rsc.hatenablog.com/entry/20150421/1429565155
