# Question 5，the output is on the github
# As based on a squared grid, it is obvious to see the adjacent of corner point is two, the adjacent of edge is three
# and adjacent of inner point is four. For N square grid, there are four vertex point, (N-2)*4 edge points and 4*N-4 inner points.
# For N*N grid, it has N^2 points and 4*(N-1)+2(N-1)(N-2) edges
# I tried Ant colony optimization, Simulated annealing,Genetic Algorithm.I finally chose Tabu Search seached from Internet. I managed
# to build the model and the Tabu search but failed to calculated the final result.

# I conctruct my map like:

# 1 2 3 ...
# 65 66 67 ...
# 129 130 131 ...
# ...
# 4033 4034 4035 ...

# I choose to put the blue beads in the 45 degrees line, which will ocst 1056 blue beads, like:

# B * ...
# * B * ...
# B * B * ...
# * B * B * ...
# B * B * B * ...
# * B * B * B * ...

def buildmap(N):
    edge = 0
    edges = 4*(N-1) + 2*(N-1)*(N-2)
    #print(edges)                          # make sure each edge is in consideration
    arr=[]
    arr.append('p')
    arr.append('edge')
    arr.append(N**2)
    arr.append(edges)
    str0 = ' '.join(str(i) for i in arr)
    with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt',"a") as f:
                text=f.write(str(str0)+"\n")
    f.close()
    for i in range(1,N**2+1):
        arr = []
        arr1 = []
        # the last column in one row
        if (i%N == 0):
            arr.append('e')
            arr.append(i)
            arr.append(i+N)
            str0 = ' '.join(str(i) for i in arr)
            with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt',"a") as f:
                text=f.write(str(str0)+"\n")
            f.close()
            #np.savetxt('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/input.txt',arr)
            edge += 1
            #print('1',edge)

        # not the last column in one row
        elif (i%N != 0 and i < (N**2-N+1)):
            arr.append('e')
            arr.append(i)
            arr.append(i+1)
            arr1.append('e')
            arr1.append(i)
            arr1.append(i+N)
            str0 = ' '.join(str(i) for i in arr)
            str1 = ' '.join(str(i) for i in arr1)
            with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt',"a") as f:
                text=f.write(str(str0)+"\n")
            f.close()
            with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt',"a") as f:
                text=f.write(str(str1)+"\n")
            f.close()
            edge += 2
           #print('2',edge)

        # the last row in map
        elif (i%N != 0 and (N**2-N+1)<= i <= N**2):
            arr.append('e')
            arr.append(i)
            arr.append(i+1)
            str0 = ' '.join(str(i) for i in arr)
            with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt',"a") as f:
                text=f.write(str(str0)+"\n")
            f.close()
            edge += 1
            #print('3',edge)

        if(edge == edges):
            print("finish")
            break

def getAdjMatrix(path):
    edge = []
    pointNum = 0
    with open(path, 'r') as fp:
        for line in fp.readlines():
            if line.startswith('p'):
                pointNum = int(line.split()[2])
                print('pointNum:',pointNum)
                for i in range(pointNum):
                    edge.append([0 for i in range(pointNum)])
            if line.startswith('e') and pointNum > 0:
                edge[int(line.split()[1]) - 1][int(line.split()[2]) - 1] = 1
                edge[int(line.split()[2]) - 1][int(line.split()[1]) - 1] = 1
                print('edge:',edge)
    return edge, pointNum


# buildmap(L)
buildmap(64)
edge, pointNum = getAdjMatrix(r'C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 5_半完成/map.txt')
print('')
#     for i in edge:
#         print('    ', end='')
#         for j in i:
#             print(j, end='\t\t')
#         print('\n')
colorNum = 0
disabled = []

# color[] is used to record each point's color
color = []
for i in range(pointNum):
    color.append(0)
edgeNum = [sum(e) for e in edge]
for k in range(pointNum):
    # record the point which has the max edge
    maxEdgePoint = [i for i in range(pointNum) if edgeNum[i] == max(edgeNum) and edgeNum[i] != 0]
    
    for p in maxEdgePoint:
        if p not in disabled:
            # select those points which has no color
            color[p] = colorNum + 1
            disabled.append(p)
            edgeNum[p] = 0
            # temp is used to find out the next uncolored point
            temp = edge[p]
            for i in range(pointNum):
                 if i not in disabled:
                    if temp[i] == 0:
                        # avoid the same color
                        color[i] = colorNum + 1
                        disabled.append(i)
                        edgeNum[i] = 0
                        # add Tabu node of current color
                        temp = [x + y for (x, y) in zip(edge[i], temp)]
            # if the new color is needed
            colorNum = colorNum + 1

    # check whether every point has color
    if 0 not in color:
        break
        
print(color)
print(colorNum)


