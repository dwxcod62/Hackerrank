dm = list(map(int, input().rstrip().split()))
n=dm[0]
m=dm[1]
t=(m-7)//2
k=(n//2)+1
for i in range (1,n+1):
    if i==k:        
        print('-'*t+'WELCOME'+'-'*t)
    elif(i<k):
        print('---'*(k-i)+('.|.'*(i))+('.|.'*(i-1))+('---'*(k-i)))
    else:
        print(('---'*(i-k))+('.|.'*(n-i+1))+('.|.'*(n-i))+('---'*(i-k)))