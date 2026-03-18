n = int(input())
arr = [ ]
for i in range(n):
    arr.append(int(input()))
count = 0
max_val = 0
for i in range (n):
    if arr[i] > max_val:
        count += 1
        max_val=arr[i]
        
print(count)
