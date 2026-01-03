n=int(input())
arr = []
full= []
empty= []
for _ in range(n):
    x = int(input())
    if x!= 0:
        full.append(x)
    else:
        empty.append(x)
result=full+empty             
print(*result)
print("ALL FULL PACKS  ARE IN THE FIRST AND THE EMPTY  PACKS IN THE LAST ROW ")

