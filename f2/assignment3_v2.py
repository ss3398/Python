import numpy as np
from sklearn.linear_model import LinearRegression

from copy import deepcopy
from sklearn.impute import SimpleImputer

############################################################
# Problem 1: Gauss-Jordan Elimination
############################################################

# function to exchange rows i and j. This function is used in the main Gauss jordan function
def exchg_row(D,i,j):
    D[j], D[i] = D[i], D[j]
    return D

# Function to check for all 0s. Used in main JDE
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

# Main JDE function of Problem 1
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

    #check to see if this is square matrix
    if(rows!=cols):
      print("cannot invert a non-square matrix")
      blankRet = None
      return blankRet

    #check if this is an invertible matrix. if determinent is zero then it is not invertible 
    if(np.linalg.det(A) == 0):
        blankRet = None
        return blankRet

    # As a first steo, get the identity matrix and append it to the right of A
    # This, in accordance with GJE algo, is done because our row operations will make the identity into the inverse
    #attaching identity to the Right:
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
#below is to get rid of the identity matrix on Left:
    for i in range(0,rows):
        A[i] = A[i][cols:len(A[i])]

    return A

    
############################################################
# Problem 2: Ordinary Least Squares Linear Regression
############################################################

#problem 2, part 1:
def linear_regression_inverse(X,y):
    return ((np.linalg.inv((X.transpose()).dot(X))).dot(X.transpose())).dot(y)

#problem 2, part 2:
def linear_regression_moore_penrose(X,y):
    return (np.linalg.pinv(X)).dot(y)

#problem 3
# Report the shape of the array, the total number of NaN values
#in the array, and the mean and standard deviation of each #numerical #feature (ignoring NaN values). If there are #categorical features (strings or integers), please report the #number of distinct values for each such feature.
def report_on_array(X):
    print(X.shape)
    print(np.isnan(X).sum())
    print(np.nanmean(X))
    print(np.nanstd(X))
    print(np.count_nonzero(np.unique(X,False)))
    print(np.unique(X, return_counts=True))

# replace NaN with mean of the column. Works for numeric.
def clean_and_save_data_numeric(X):
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(X)
    return imp.transform(X)

# replace NaN with most frequent value. Works for strings.
def clean_and_save_data_text(X):
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    return imp.fit_transform(X)

    
def generate_data(n,m):
    """
        Generates a synthetic data matrix X of size n by m
        and a length n response vector.

        Input:
            n - Integer number of data cases.
            m - Integer number of independent variables.

        Output:
            X - n by m numpy array containing independent variable
                observasions.
            y - length n numpy array containg dependent variable
                observations.
    """
    X = np.random.randn(n, m)
    beta = np.random.randn(m)
    epsilon = np.random.randn(n)*0.5
    y = np.dot(X, beta) + epsilon

    return X, y


if __name__=="__main__":
    # test gauss-jordan elimination
    X = np.random.randn(3, 3)
    print(np.allclose(gauss_jordan(X), np.linalg.inv(X)))

    # test linear regression
    X, y = generate_data(10, 3)
    lr = LinearRegression(fit_intercept=False)
    lr.fit(X, y)
    beta = lr.coef_
    #print(np.allclose(linear_regression_inverse(X, y), beta))
    print(np.allclose(linear_regression_moore_penrose(X,y), beta))
    #print("printing x")
    #print(X)
    #print("printing y")
    #print(y)
    #print("beta")    
    #print(beta)
    #print("printing penrose")    
    #print(linear_regression_moore_penrose(X,y))
