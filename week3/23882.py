import sys
input=sys.stdin.readline

A, K = map(int, input().split())

list = list(map(int, input().split()))
count = 0

for i in range(A-1, 0, -1):
    index = list.index(max(list[:i+1]))
    if index != i:
        list[index], list[i] = list[i], list[index]
        count += 1
        if count == K:
            for j in list:
                print(j, end=' ')
                
if K > count:
    print(-1)
