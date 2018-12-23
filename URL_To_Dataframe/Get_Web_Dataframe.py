import pandas as pd
from urllib.request import urlretrieve

#--------------------
#Language: Python
#Function: get_web_dataframe()
#Purpose: Retrieve a Pandas DataFrame from a target URL containing data
#Inputs: Target url, output filename, sep condition, rows to skip, header 
#Outputs: Dataframe populated with CSV values from website data
#--------------------

def get_web_dataframe(url, filename, sep, skip, header):
    # Save file as local
    urlretrieve(url, filename)
    # Parse file into a DataFrame
    data = pd.read_csv(filename, sep=sep, skiprows=skip, header=header)
    df = pd.DataFrame(data)
    return df
