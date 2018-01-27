import pandas as pd 

#--------------------
#Language: Python
#Function: get_EDA_info()
#Purpose: Generates a series of Exploratory Data Analysis (EDA) sets from a given CSV file
#Inputs: CSV file
#Outputs: Basic EDA information for analysis
#--------------------

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
  # Print df info  
  print("Info")
  print(df.info())
  print("---------------")
  # Count and print null values
  print("Total Missing Values: " + df.isnull().sum())
  print("---------------")
