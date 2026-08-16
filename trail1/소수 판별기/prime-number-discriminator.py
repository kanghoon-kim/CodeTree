N = int(input())
ck = False
for i in range(2,N):
    if N%i ==0:
        ck = True
        break

if ck == True:
    print("C")
else:
    print("P")
