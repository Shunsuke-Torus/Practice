def bubblesort(int_list):
    for i in range (len(int_list)-1,0,-1):
        for j in range(i):
            if int_list[j] > int_list[j+1]:
                int_list[j],int_list[j+1] = int_list[j+1],int_list[j]
                
    print("Soreted")
    return int_list
    
import random
import time

start_time = time.perf_counter()       # 処理前の時刻
int_list= [random.randint(0,100)for i in range(100)]


print(bubblesort(int_list))
elapsed_time = time.perf_counter() - start_time

print("elapsed_time =",elapsed_time)
