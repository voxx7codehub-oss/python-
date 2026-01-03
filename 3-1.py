n=int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

count0=arr.count(0)
count1=arr.count(1)
count2=arr.count(2)
result=[0]*count0+[1]*count1+[2]*count2               
print(result)
