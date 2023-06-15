import time
st = time.time()



def partition(list,l,h):

    pivot =list[h]
    i = l - 1
    for j in range(l,h):
        if list[j] <= pivot:
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
 
    (list[i + 1], list[h]) = (list[h], list[i + 1])
    return i + 1
 
 
def quickSort(list, l, h):
    if l<h:

        pi = partition(list, l, h)
        quickSort(list, l, pi - 1)
        quickSort(list, pi + 1, h)
import random
data = []
for i in range(4902939):
    #x=random.randrange(0, 500000339783)
    data.append(i)

 
size = len(data)
 
quickSort(data, 0, size - 1)
print(data)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
