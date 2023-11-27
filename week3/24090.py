# 퀵 정렬 -> 분할 정복(divide and conquer) 방법
# 문제를 작은 2개의 문제로 분리 &  각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
# 기준값과 비교하여,  오른쪽 왼쪽 분리 
# 기준을 바꿔가면서 정렬 계속 진행
# 리스트의 분할이 더 이상 불가능할때까지 진행
# 분할 /정복 / 결합
# https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html (참고 링크)

import sys
input=sys.stdin.readline

A1, A2 = map(int,input().split())
K = list(map(int,input().split()))

# 출력값이 이해가 안 가서 .. 좀만 더 이해해보고 싶어요 
# 알듯말듯 .. 