from copy import deepcopy

def check_for_all_zeros(X,i,j):
    non_zeros = []
    first_non_zero = -1
    for m in range(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero

def swap_row(X,i,p):
    X[p], X[i] = X[i], X[p]
    return X

def make_identity(r,c):
    identity = []
    for i in range(0,r):
        row = []
        for j in range(0,c):
            elem = 0
            if i==j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return identity


def gje_invert(X):
    """
    Invert a matrix X according to gauss-jordan elimination
    X - input list of lists where each list is a matrix row
    output - inverse of X
    """
    #copy X to avoid altering input
    X = deepcopy(X)

    #Get dimensions of X
    rows = len(X)
    cols = len(X[0])

    #Get the identity matrix and append it to the right of X
    #This is done because our row operations will make the identity into the inverse
    identity = make_identity(rows,cols)
    for i in range(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in range(0,cols):
        #print("On col {0} and row {1}".format(j,i))
        #Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)
        #If everything is zero, increment the columns
        if zero_sum==0:
            if j==cols:
                return X
            continue
        #If X[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            X = swap_row(X,i,first_non_zero)
        X[i] = [m/X[i][j] for m in X[i]]
        for q in range(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in range(0,len(scaled_row))]
        if i==rows or j==cols:
            break
        #print (X)
        i+=1

    for i in range(0,rows):
        X[i] = X[i][cols:len(X[i])]

    return X



print(gje_invert([[1,3,3],[1,4,3],[1,3,4]]))
print(gje_invert([[1,0,0],[0,1,0],[0,0,1]]))


