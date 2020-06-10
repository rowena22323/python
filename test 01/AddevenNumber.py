import numpy as np
list = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]

arr = np.array(list).reshape(1,12)

sum=0
i=0
for i in np.nditer(arr):
    if(i%2==0):
        sum+=i

print(sum)