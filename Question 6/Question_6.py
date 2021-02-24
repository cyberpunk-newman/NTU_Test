# Question 6
# First read the point and polygon from txt file, transfer into list. Each time in for loop, it will check 
# whether the point is in polygon or not.In the function <b>in_poly(p,poly)</b>, px and py store the coodinate
# of point respectively. <b>is_in</b> is False in default. (x1,y1) is first vertex and (x2,y2) is next vertex. 
# I first check whether the point is on the vertex. Then after checking <b>py</b> is between vertices, seeing 
# whether the <b>point</b> has an intersection with the horizontal right ray. If there is, the <b>is_in</b> will be reversed.


import numpy as np

def in_poly(p, poly):
    
    px, py = p
    is_in = False
    for i, vertices in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = vertices
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in
 
 
if __name__ == '__main__':
    point = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 6/input_question_6_points.txt')
    poly = np.loadtxt('C:/Users/RM.Z/Desktop/SO金牌/NTU/Question 6/input_question_6_polygon.txt')
    #print(type(a))
    point = point.tolist()
    #print(type(a))
    poly = poly.tolist()
    
    for i in range(10):
        cur_point = point[i]
        if in_poly(cur_point, poly) is True:
            for i in range(2):
                print(round(cur_point[i]),end=' ')
            print("inside")
            
        else:
            for i in range(2):
                print(round(cur_point[i]),end=' ')
            print("outside")
        