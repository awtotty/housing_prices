import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warning.filterwarning('ignore')


# Import training data
df_train = pd.read_csv('../input/train.csv')

df_train.columns