# main.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv('aapl_stock_data.csv')

# Feature engineering and model training logic goes here
print("Project is set up and ready to code!")
