#ソートを書いてみる

def bubblesort(int_list):
    for index in range (len(int_list)-1,0,-1):
        for low in range(index):
            if int_list[low] > int_list[low+1]:
                tmp = int_list[low+1]
                int_list[low+1] = int_list[low]
                int_list[low] = tmp
    print("Soreted")
    return int_list
    
import random
import time

start_time = time.perf_counter()       #Before time
int_list= [random.randint(0,100)for i in range(100)]


print(bubblesort(int_list))
elapsed_time = time.perf_counter() - start_time #After time

print("elapsed_time =",elapsed_time)
