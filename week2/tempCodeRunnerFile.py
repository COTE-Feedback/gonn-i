import sys
input=sys.stdin.readline

N,K = map(int, input().split())
list = [] #출력용 리스트
sit = [i for i in range(1+ N+1)] #실제 앉아 있는 모습
num = 0

for i in range(N):
    num+= K -1
    if num >= len(sit):
        num %= len(sit)
        
    list.append(str(sit[num]))
    sit.pop(num)

# ', '.join(list) 리스트의 각 항목을 쉼표와 공백으로 연결
print("<",', '.join(list),">", sep="")