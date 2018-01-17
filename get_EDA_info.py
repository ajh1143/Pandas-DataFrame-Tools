import pandas as pd 

def get_EDA_info(filename):
  # Load DataFrame as df
  csv = pd.read_csv(filename)
  df = pd.DataFrame(csv)
  # Print shape of df
  print(df.shape)
  # Print all cols in df
  print(df.columns)
  # Print the top results of df cols
  print(df.head())
  # Print the bottom results of df cols
  print(df.tail())
  # Count and print null values
  print("Total Missing Values: " + df.isnull().sum())
