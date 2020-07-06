mat=[[2,7,6],[9,5,1],[4,3,8]]
l=len(mat)
index=[0]*l*l
flag=1
for i in range(l):
    for j in range(l):
        if index[mat[i][j]-1]==0:
            index[mat[i][j]-1]+=1
        else:
            flag=0
if flag:
    print("MAGICNUMBER")
            
