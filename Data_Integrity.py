#--------------------
#Language: Python
#Function: replace_with_mean()
#Purpose: Replaces NA observations in specified column with mean of populated column
#Inputs: Pandas DataFrame, Target Column Name
#Outputs: Dataframe with missing values imputed to average
#--------------------

def replace_with_mean(df, colname):
    col_mean = np.mean(df[colname])
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
    pre_col =  pd.DataFrame(df[cols])
    print(pre_col.info())
    post_col = pre_col.drop_duplicates()
    print(post_col.info())
    return post_col

