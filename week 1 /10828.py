import sys
input=sys.stdin.readline
#시간 초과로 인해 추가
# input 대신에 값을 입력받는 데 더 빠르다고 함

command_count = int(input())
stack = []

for i in range(command_count):
    command = list(map(str, input().split()))
    
    if command[0]== 'push':
        stack.append(int(command[1]))
        
    elif command[0] == 'pop':
        if (len(stack) != 0):
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
        else: print(-1)
    elif command[0] == 'size': 
        print(len(stack))
        
    elif command[0] == 'empty':
        if (len(stack) == 0):
            print(1)
        else: print(0)
        
    elif command[0] == 'top':
        if (len(stack) == 0):
            print(-1)
        else: print(stack[len(stack)-1])