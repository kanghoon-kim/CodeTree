N = int(input())

cnt = 0
while True:
    if N  == 2**cnt:
        print(cnt)
        break
    cnt += 1