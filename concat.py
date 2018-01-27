#--------------------
#Language: Python
#Function: concat()
#Purpose: Concatenates a series of Pandas DataFrames
#Inputs: list of Pandas DataFrames
#Outputs: Concatenated DataFrame
#--------------------

def concat(df_list):
    df_output = pd.concat(df_list)
    print(df_output.shape)
    print(df_output.head())
    return df_output
