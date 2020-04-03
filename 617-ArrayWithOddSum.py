test = int(input())
sum = 0
a=[]
while test>=0:
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    j=0
    for i in range(len(a)):
        if(i>=1 and j<=n):
            if(i!=j):
                a[i]=a[j]
        j+=1
    for i in range(len(a)):
        sum+=a[i]
    test=test-1
if(sum%2!=0):
    print("YES")
else:
    print("NO")
