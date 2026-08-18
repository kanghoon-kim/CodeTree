N = int(input())
cur= 1
for i in range(1,N+1):
    
    if i%2 != 0:
        for j in range(1,N+1):
            print(cur,end=" ")
            cur += 1
    elif i%2==0:
        cur += N-1
        for j in range(1,N+1):
            #역방향 출력
           
            print(cur,end=" ")
            cur -= 1
        cur += N + 1
    print()
        

            