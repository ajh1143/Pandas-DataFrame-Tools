import pandas as pd
from urllib.request import urlretrieve

def get_web_dataframe(url, filename, sep, skip, header):
    # Save file as local
    urlretrieve(url, filename)
    # Parse file into a DataFrame
    data = pd.read_csv(filename, sep=sep, skiprows=skip, header=header)
    df = pd.DataFrame(data)
    return df
