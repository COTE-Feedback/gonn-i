import sys
input=sys.stdin.readline


n = int(input()) 
people = list(map(int, input().split()))  
answer = 0

people.sort()  # 오래 걸리는 사람 제일 뒤로 보내기 

for x in range(1, n+1):
    answer += sum(people[:x])  
    
print(answer)  