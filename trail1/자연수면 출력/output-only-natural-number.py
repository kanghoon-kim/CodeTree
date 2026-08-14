a,b = map(str,input().split())
b = int(b)
if int(a) > 0:
    for i in range(b):
        print(a,end = "")
else:
    print(0)
