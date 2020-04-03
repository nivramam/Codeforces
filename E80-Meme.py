def checkEqual(LHS,RHS):
    if(str(LHS)==RHS):
        return True
    return False
 
 
testcases = int(input())
cnt = 0
lis= []
while(testcases>0):
    # print('hi')
    A,B = input().split()
    A = int(A)
    B = int(B)
    a=1
    b=1
    for a in range(A):
        for b in range(B):
            LHS = (a*b) + a+b
            RHS = str(a) + str(b)
            result = checkEqual(LHS,RHS)
            if(result==True):
                cnt+=1
    lis.append(cnt)
    testcases=testcases-1
for i in range(len(lis)):
    print(lis[i])
