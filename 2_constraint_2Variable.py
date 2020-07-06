#list of all the corner points
b = [[1,0],[0,1]]

#list of all the d values calcualted
d = list()
v = [[5,2],[3,5]]
w = [2,5]
def sol_primal_LP(v,w,e):
    """
    inputs are the given values as mentioned in the algorithm
    u1,u2 and w2 are the lsit of 2 dimension
    """
    u1 = v[0]
    u2 = v[1]
    # if the denominator is not equal to zero then we will add this
    # in the corner point list
    if (u1[1]-u1[0]+u2[0]-u2[1]) != 0:
        b1 = (u1[1] - u2[1])/(u1[1]-u1[0]+u2[0]-u2[1])
        b2 = 1 - b1
        b.append([b1,b2])
    
    #loop through all the corner points stored in b and store it the d values
    for i in b:
        d.append(i[0](w[0] - u1[0]) + i[1](w[1] - u1[2]))
        
    return max(d)

sol_primal_LP(v,w,0)


    