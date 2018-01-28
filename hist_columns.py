import pandas as pd
import matplotlib.pyplot as plt

#--------------------
#Language: Python
#Function: hist_columns()
#Purpose: Easily generate a Histogram pyplot from a DataFrame and list of columns 
#Inputs: Pandas DataFrame, Log condition(T/F), Rotation value, single or variable column names
#Outputs: Histogram plots of given column in Pandas DataFrame
#--------------------

def hist_columns(df, log, rot, *args):
    # For each column name given, check if log axes chosen, plot histogram
    for arg in args:
        #Check if user passed a logarithmic scale designation
        if log == "True":
            #Create Histogram plot
            df[arg].plot(kind='hist', logx=True, logy=True, rot=rot)
            #Add x-axis label
            plt.xlabel(str(arg))
            #Show plot
            plt.show()
        #No log scale specified
        else:
            #Create Histogram plot
            df[arg].plot(kind='hist', logx=False, logy=False, rot=rot)
            #Add x-axis label
            plt.xlabel(str(arg))
            #Show plot
            plt.show()
