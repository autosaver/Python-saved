arr=[0,-1,2,-3,1,4,5,6,7,-2,-6]
l=len(arr)
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            if arr[i]+arr[j]+arr[k]==0:
                print(arr[i],arr[j],arr[k])
