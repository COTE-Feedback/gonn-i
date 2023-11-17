import sys
input=sys.stdin.readline
from collections import deque

command_num = int(input())
d =deque()
for e in range (0,command_num):
    command = input().split()
    if (command[0] == 'push_front'): d.appendleft(command[1])
    elif (command[0]=='push_back'): d.append(command[1])
    elif (command[0] =='pop_front'):
        if(len(d) ==0 ): print(-1)
        else: 
            print(d[0])
            d.popleft() 
    elif (command[0] =='pop_back'):
        if(len(d) ==0 ): print(-1)
        else:
            print(d[len(d)-1]) 
            d.pop()
    elif (command[0] =='size'):
        print(len(d))
    elif (command[0] =='empty'):
        if(len(d)!= 0): print(0)
        else: print(1)
    elif (command[0] =='front'):
        if(len(d)== 0): print(-1)
        else: print(d[0])
    elif (command[0] =='back'):
        if(len(d)== 0): print(-1)
        else: print(d[len(d)-1])
        