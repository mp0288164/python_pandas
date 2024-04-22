#import pandas and numpy
import pandas as pd
import numpy as np
#tile() method of numpy. tile method are copy value
arr=np.tile([12,34],3)
obj1=pd.Series(arr)
print(obj1)