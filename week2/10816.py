import sys
from collections import Counter
input=sys.stdin.readline

N = int(input())
Ncards = sorted(list(map(int,input().split())))
M = int(input())
Mcards = list(map(int,input().split()))

# counter 는 리스트를 값으로 주어진 원소가 몇번 등장하는지 딕셔너리 형태로 반환
# >>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})
count = Counter(Ncards)


for e in range (0,M):
    if Mcards[e] in count:
        print(count[Mcards[e]] ,end=' ')  #/n 개행없이 출력
    else: print(0 , end=' ')

