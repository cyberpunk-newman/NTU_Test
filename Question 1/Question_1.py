# Question 1

# matrix() is used to calculat the summed number which is for sure
# a is a*b matrix 
def matrix(a,b):
    j = 0
    for i in range(1,a+1):
        j+=i
    return j

res = []

# total_sum(summed_number-Matrix)
def total_sum(M,arr=[]):
    if M==0:
        res.append(arr)
        return
    if M<0:
        return
    total_sum(M-1,arr+[1])
    total_sum(M-2,arr+[2])
    total_sum(M-3,arr+[3])
    total_sum(M-4,arr+[4])
    total_sum(M-5,arr+[5])
    total_sum(M-6,arr+[6])
    total_sum(M-7,arr+[7])
    total_sum(M-8,arr+[8])
    total_sum(M-9,arr+[9])

# get(summed number,N)    N: N*N squared matrix 
def getsquarematrix(num,N):
    N = N-1
    for i in res:
        last = ''.join([str(j) for j in i])
        if len(last) == N:
            result = last.split(' ')
            for a in range (1,N+2):
                a = str(a)
                result.append(a)

            final = ''.join(result)
    c = sorted(final)
    M = N+1
    print(num,end=' ')
    for i in range (1,2*M-1):
        if c[i]==c[i-1]:
            print('R',end='')
        else:
            print('D',end='')
            
            
# get(summed_number,N,M)    N,M: N*M rectangle matrix 
def getrectanglematrix(num,N,M):
    k = M+1
    for i in res:
        last = ''.join([str(j) for j in i])
        if len(last) == k:
            result = last.split(' ')
            for a in range (1,k+N):
                a = str(a)
                result.append(a)

            final = ''.join(result)
    c = sorted(final)
    print(num,end=' ')
    for i in range (1,N+M-1):
        if c[i]==c[i-1]:
            print('R',end='')
        else:
            print('D',end='')
    


total_sum(65-matrix(9,9))
getsquarematrix(65,9)

total_sum(72-matrix(9))
getsquarematrix(72,9)

total_sum(90-matrix(9))
getsquarematrix(90,9)

total_sum(110-matrix(9))
getsquarematrix(110,9)

total_sum(87127231192-matrix(90000,100000))
getrectanglematrix(87127231192,90000,100000)

total_sum(5994891682-matrix(90000,100000))
getrectanglematrix(5994891682.,90000,100000)
