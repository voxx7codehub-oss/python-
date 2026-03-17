n=int(input())
l = [ ]
for i in range(n):
    l.append(int(input()))
psum=0
nsum=0
zsum=0
for i    in l :
    if i>0:
        psum=psum+i
    elif i<0:
        nsum=nsum+i
    else:
        zsum=zsum+i
print("%f"%(psum/n))
print("%f"%(nsum/n))
print("%f"%(zsum/n))
    
