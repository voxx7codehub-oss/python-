n = int(input().strip())
state = list(map(int, input().split()))
dist = list(map(int, input().split()))
n = min(n, len(state), len(dist))
state = state[:n]
dist = dist[:n]
on = [i for i in range(n) if state[i] == 1]
if not on:
    print(0)
    exit()
total = 0
for i in range(n):
    if state[i] == 0:
        nearest = min(abs(dist[i] - dist[j]) for j in on)
        total += nearest
        on.append(i)
print(total)
