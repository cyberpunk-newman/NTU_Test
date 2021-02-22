#7.1 b)
import numpy as np

def coord2index(arr):
    index = 50*arr[1] + arr[0]
    return int(index)


def index2coord(index):
    x2 = index // 50
    x1 = index - 50*x2
    return int(x1),int(x2)

index = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 7/Question 7.1/input_index_7_1.txt',skiprows=1)
coord = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 7/Question 7.1/input_coordinates_7_1.txt',skiprows=1)

#print(index.shape)   #total 1425 data
#print()
#print(coord.shape)    #total 1425 data

for i in range(1425):
    result4coord = coord2index(coord[i])
    #print(result4coord)
    with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 7/Question 7.1/output_index_7_1.txt',"a") as f:
        text=f.write(str(result4coord)+"\n")
    f.close()



for i in range(1425):
    result4index = index2coord(index[i])
    #print(result4index)
    with open('C:/Users/RM.Z/Desktop/SO金牌/南洋理工笔试题/Question 7/Question 7.1/output_coordinates_7_1.txt',"a") as f:
        text=f.write(str(result4index[0])+"    "+str(result4index[1])+"\n")
    f.close()




