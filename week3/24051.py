import sys
input=sys.stdin.readline

A1, A2 = map(int,input().split())
K = list(map(int,input().split()))

tmp = 0

for i in range(1, len(K)):
    tmp = K[i]
    j = i
    while K[j - 1] > tmp:
        A2 -= 1
        K[j] = K[j - 1]
        j -= 1
        if A2 == 0:
            print(K[j])
        if j - 1 < 0:
            break

    if j != i:
        K[j] = tmp
        A2 -= 1
        if A2 == 0:
            print(K[j])

if A2 > 0:
    print(-1)

