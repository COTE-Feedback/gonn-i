from collections import deque

import sys
input=sys.stdin.readline

N = int(input())
card = list(range(1,N+1))
card = deque(card)

while(1):
    if (len(card) == 1 ):
        print(card[0])
        break
    else: 
        card.popleft()
        card.append(card.popleft())
        continue
