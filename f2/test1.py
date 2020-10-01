import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.impute import SimpleImputer
import csv

A = np.array(([2,3,0],[1,-2,-1],[2,-4,-2]))

try:
  print(np.linalg.inv(A))
except:
  print("An exception occurred")
  


