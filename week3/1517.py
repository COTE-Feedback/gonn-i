import sys
input=sys.stdin.readline

def bubble(li):
    global count
    end = len(li) - 1
    while end > 0:
        last = 0
        for i in range(end):
            if li[i] > li[i + 1]:
                count += 1
                li[i], li[i + 1] = li[i + 1], li[i]
                last= i
        end = last

swap_count = 0
N = int(input())
list = list(map(int, input().split()))
count =0

bubble(list)
print(count)
# 시간초과 엔딩 - 도무지 모르겠음 플레 