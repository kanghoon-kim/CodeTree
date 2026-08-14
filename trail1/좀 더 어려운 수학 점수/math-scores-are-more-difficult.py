Mat_a , Eng_a = map(int,input().split())
Mat_b , Eng_b = map(int,input().split())

if Mat_a > Mat_b or (Mat_a == Mat_b and Eng_a>Eng_b):
    print("A")
else:
    print("B")
