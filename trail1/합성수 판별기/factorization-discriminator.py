N = int(input())
checker = False
for i in range(2,N):
    if N % i == 0:
        checker = True
        break

if checker == True:
    print("C")
else:
    print("N")
