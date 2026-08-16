sum = 0
cnt = 0
while True:
    N = int(input())
    
    
    if N < 20 or 30<= N  :
        
        avg = sum/cnt

        print(f"{avg:.2f}")

        break
    sum += N
    

    cnt += 1
    
    
   
        