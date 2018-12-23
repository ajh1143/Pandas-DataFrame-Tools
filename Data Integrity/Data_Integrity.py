#--------------------
#Language: Python
#Function: replace_with_mean()
#Purpose: Replaces NA observations in specified column with mean of populated column
#Inputs: Pandas DataFrame, Target Column Name
#Outputs: Dataframe with missing values imputed to average
#--------------------

def replace_with_mean(df, colname):
    #Generate mean values of specified column
    col_mean = np.mean(df[colname])
    #Add mean values to DataFrame.colname
    df[colname] = df[colname].fillna(col_mean)
    print(df.info())
    return df

#--------------------
#Language: Python
#Function: check_missing_data()
#Purpose: Tests if dataframe has missing data via Assert statement
#Inputs: Pandas DataFrame
#Outputs: Throws error if index values are null/missing
#--------------------

def check_missing_data(df):
    #Test assertion of null values
    assert pd.notnull(df).all().all()

       
#--------------------
#Language: Python
#Function: drop_dups()
#Purpose: Drops duplicates from specified column
#Inputs: Pandas DataFrame, Target Column Name
#Outputs: Cleaned DataFrame, duplicate entries expunged
#--------------------
    
#DROP DUPLICATES FROM A DEFINED COLUMN = cols OF DATAFRAME = df
def drop_dups(df, cols):
    #Generate a pre-processed representation of specified column
    pre_col =  pd.DataFrame(df[cols])
    #Check column info
    print(pre_col.info())
    #Drop any duplicate rows within pre_col
    post_col = pre_col.drop_duplicates()
    #Check if successful
    print(post_col.info())
    #Return the processed DataFrame
    return post_col

