def concat(df_list):
    df_output = pd.concat(df_list)
    print(df_output.shape)
    print(df_output.head())
    return df_output
