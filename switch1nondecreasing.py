inputs=[4,2,3,1]
n=len(inputs)
flag=0
for i in range(n-1):
    if inputs[i]>inputs[i+1]:
        flag+=1
print(flag)
