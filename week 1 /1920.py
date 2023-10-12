import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = input()
array_m = list(map(int,input().split()))

A.sort()

for i in array_m:
    start, end = 0, N-1
    exist = False
    
    while (start <= end ):
        mid = (start + end) // 2
        if i == A[mid]:
            print(1)
            exist = True
            break
        elif i > A[mid]:
            start = mid +1
        else:
            end = mid -1
        
    if not exist: 
        print(0)