import pandas as pd
import matplotlib.pyplot as plt

#Input a dataframe, a single column name, a list of col names, or multiple arguments to retrieve
#histogram plots for each. Define log as True or False to use log axes, and define rotation

def hist_columns(df, log, rot, *args):
    # For each column name given, check if log axes chosen, plot histogram
    for arg in args:
        if log == "True":
            df[arg].plot(kind='hist', logx=True, logy=True, rot=rot)
            plt.show()
        else:
            df[arg].plot(kind='hist', logx=False, logy=False, rot=rot)
            plt.show()
