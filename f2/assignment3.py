import numpy as np
import numpy.linalg as la
from sklearn.linear_model import LinearRegression
import unittest

############################################################
# Problem 1: Gauss-Jordan Elimination
############################################################

def gauss_jordan(A):
    ## Add code here ##
    return -1

    
############################################################
# Problem 2: Ordinary Least Squares Linear Regression
############################################################

def linear_regression_inverse(X,y):
    ## Add code here ##
    return -1
    
def linear_regression_moore_penrose(X,y):
    ## Add code here ##
    return -1
    
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
    print(np.allclose(gauss_jordan(X), la.inv(X)))

    # test linear regression
    X, y = generate_data(10, 3)
    lr = LinearRegression(fit_intercept=False)
    lr.fit(X, y)
    beta = lr.coef_
    print(np.allclose(linear_regression_inverse(X, y), beta))
    print(np.allclose(linear_regression_moore_penrose(X, y), beta))
