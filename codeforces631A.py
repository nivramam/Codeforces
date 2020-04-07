testcases = int(input())
cnt=0
items=[]
while(testcases!=0):
    n,x = input().split()
    n = int(n)
    x = int(x)
    # print("n :",n)
    # print("x :",x)
    for i in range(n):
        items.append(int(input()))
    for i in range(n):
        if(items[i]>=1 and items[i]<=x):
            cnt+=1
    v = x - cnt
    testcases = testcases - 1
    print("v: ",v)
