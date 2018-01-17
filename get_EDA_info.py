import pandas as pd 

def get_EDA_info(filename):
  # Load DataFrame as df
  csv = pd.read_csv(filename)
  df = pd.DataFrame(csv)
  # Print shape of df
  print("Shape")
  print(df.shape)
  print("---------------")
  # Print all cols in df
  print("Columns")
  print(df.columns)
  print("---------------")
  # Print the top results of df cols
  print("Head")
  print(df.head())
  print("---------------")
  # Print the bottom results of df cols
  print("Tail")
  print(df.tail())
  print("---------------")
  # Count and print null values
  print("Total Missing Values: " + df.isnull().sum())
  print("---------------")
  # Print df info  
  print("Info")
  print(df.info())
  print("---------------")

