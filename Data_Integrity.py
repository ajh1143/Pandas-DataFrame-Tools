#MISSING DATA

#REPLACES NA OBSERVATIONS IN COLUMN = colname OF DATAFRAME = df WITH MEAN OF POPULATED COLUMN
def replace_with_mean(df, colname):
    col_mean = np.mean(df[colname])
    df[colname] = df[colname].fillna(col_mean)
    print(df.info())
    return df
    
#ASSERT MISSING DATA
def check_missing_data(df):
    assert pd.notnull(df).all().all()

    
    
#DUPLICATE DATA
    
#DROP DUPLICATES FROM A DEFINED COLUMN = cols OF DATAFRAME = df
def drop_dups(df, cols):
    pre_col =  pd.DataFrame(df[cols])
    print(pre_col.info())
    post_col = pre_col.drop_duplicates()
    print(post_col.info())
    return post_col

