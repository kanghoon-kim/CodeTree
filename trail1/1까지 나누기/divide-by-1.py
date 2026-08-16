N = int(input())
cnt = 0
while True:
    if N <= 1:
        print(cnt)
        break
    cnt += 1
    N = N//cnt
    
    
    