a = int(input())
spot = []
for i in range(a):
	(m,n) = list(map(int, input().split()))
	spot.append([m,n])

for i in sorted(spot):
	print(i[0],i[1])
