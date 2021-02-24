#7.2 b)
import numpy as np

def coord2index(arr):
    index = 8640*arr[5] + 1440*arr[4] + 160*arr[3] + 32*arr[2] + 4*arr[1] + arr[0]
    return int(index)


def index2coord(index):
    x6 = index // 8640
    x5 = (index - 8640*x6) // 1440
    x4 = (index - 8640*x6 - 1440*x5) // 160
    x3 = (index - 8640*x6 - 1440*x5 - 160*x4) // 32
    x2 = (index - 8640*x6 - 1440*x5 - 160*x4 - 32*x3) // 4
    x1 =  index - 8640*x6 - 1440*x5 - 160*x4 - 32*x3 - 4*x2
    return int(x1),int(x2),int(x3),int(x4),int(x5),int(x6)

index = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 7/Question 7.2/input_index_7_2.txt',skiprows=1)
coord = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 7/Question 7.2/input_coordinates_7_2.txt',skiprows=1)

#print(index.shape)   #total 1425 data
#print()
#print(coord.shape)    #total 1425 data

#  coord2index
for i in range(30240):
    result4coord = coord2index(coord[i])
    #print(result4coord)
    with open('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 7/Question 7.2/output_index_7_2.txt',"a") as f:
        text=f.write(str(result4coord)+"\n")
    f.close()


# #  index2coord
for i in range(30240):
    result4index = index2coord(index[i])
    #print(result4index)
    with open('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 7/Question 7.2/output_coordinates_7_2.txt',"a") as f:
        text=f.write(str(result4index[0])+"    "+str(result4index[1])+"    "+str(result4index[2])+"    "+str(result4index[3])+"    "+str(result4index[4])+"    "+str(result4index[5])+"\n")
    f.close()

print("finish")




