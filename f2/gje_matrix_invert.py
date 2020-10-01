import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.impute import SimpleImputer
import csv

def linear_regression_inverse(X,y):
    return ((np.linalg.inv((X.transpose()).dot(X))).dot(X.transpose())).dot(y)

def linear_regression_moore_penrose(X):
    return np.linalg.pinv(X)

def report_on_array(X):
    print(X.shape)
    print(np.isnan(X).sum())
    print(np.nanmean(X))
    print(np.nanstd(X))
    print(np.count_nonzero(np.unique(X,False)))
    print(np.unique(X, return_counts=True))

def clean_and_save_data_numeric(X):
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(X)
    return imp.transform(X)

def clean_and_save_data_text(X):
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    return imp.fit_transform(X)


# exchange rows i and j
def exchg_row(D,i,j):
    D[j], D[i] = D[i], D[j]
    return D

# check for all 0s
def check_0s(D,i,j):
    non_0s = []
    first_non_0 = -1
    for m in range(i,len(D)):
        non_0 = D[m][j]!=0
        non_0s.append(non_0)
        if first_non_0==-1 and non_0:
            first_non_0 = m
    sum_0 = sum(non_0s)
    return sum_0, first_non_0

# create an identity matrix of size myrow,mycol
def get_identity(myrow,mycol):
    # initialize the matrix to blank first
    retidentity = []
    for i in range(0,myrow):
        # initialize the row to blank
        idrow = []
        for j in range(0,mycol):
            idelem = 0
            # set to 0. But for diagonal elements, set to 1.
            if i==j:
                idelem = 1
            idrow.append(idelem)
        retidentity.append(idrow)
    return retidentity


"""
This function inverts a given matrix A. It uses the gauss-jordan elimination method.
"""
def gauss_jordan(A):
    #convert from numpy array to list
    A = A.tolist()
    #copy A using deepcopy to avoid altering input
    A = deepcopy(A)

    #Get dimensions of A
    rows = len(A)
    cols = len(A[0])
    
    # check that it is a square matrix
    if(rows != cols):
        blankRet = []
        return blankRet

    if(np.linalg.det(A) == 0):
        blankRet = []
        return blankRet
    
    # As a first steo, get the identity matrix and append it to the right of A
    # This, in accordance with GJE algo, is done because our row operations will make the identity into the inverse
    identitymtrx = get_identity(rows,cols)
    for i in range(0,rows):
        A[i] += identitymtrx[i]

    i = 0
    for j in range(0,cols):
        #Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_0s(A,i,j)
        #If everything is zero, increment the columns
        if zero_sum==0:
            if j==cols:
                return A
            continue
        #If A[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            A = exchg_row(A,i,first_non_zero)
        A[i] = [m/A[i][j] for m in A[i]]
        for myitr in range(0,rows):
            if myitr!=i:
                updated_row = [A[myitr][j] * m for m in A[i]]
                A[myitr]= [A[myitr][m] - updated_row[m] for m in range(0,len(updated_row))]
        if i==rows or j==cols:
            break
        i+=1

    for i in range(0,rows):
        A[i] = A[i][cols:len(A[i])]

    return A




A = np.array([[2,3,0],[1,-2,-1],[2,-4,-2]])
#A = np.array([[2,3,0],[1,-2,-1]])
print(gauss_jordan(A))

#A = np.array(([1,3,2],[2,7,7],[2,5,2]))
#y = np.array([2,-1,7])
#print(linear_regression_inverse(A,y))
#print(linear_regression_moore_penrose(np.array(([1,3,2],[2,7,7],[2,5,2]))))
#report_on_array(np.array([2,-1,7]))
#report_on_array(np.array(([1,3,2],[2,1,7],[2,5,6])))
#A = np.array(([1,7,2],[2,7,7],[2,np.nan,2]))
#print(clean_and_save_data_numeric(A))

#df = pd.DataFrame([["dog", "dog"],[np.nan, "dog"],["dog", np.nan],["dog", "cat"]], dtype="category")
#print(clean_and_save_data_text(df))

