import pandas as pd

def match_case_dataframe(df, target_labels, target_column):
    """ Search a dataframe column for specific values/strings, if match return them in a new dataframe.
        Ex. Search Column A for all rows containing 'Word'
        :param df: Pandas DataFrame containing target dataset
        :param target_labels: List of labels to be matched to observations
        :param target_column: Name of column to be assayed
        :return filtered_df : DataFrame containing observations matching target labels
    """
    if isinstance(target_labels, str):
        filtered_df = df[df[target_column].isin([target_labels])]
        print('Results:')
        find_length(filtered_df, target_labels)
        print(filtered_df.head())
        return filtered_df

    else:
        filtered_df = df[df[target_column].isin(target_labels)]
        print('Results:')
        find_length(filtered_df, target_labels)
        print(filtered_df.head())
        return filtered_df


def find_length(processed_df, target):
    """ Report how many rows matched target keyword.
        :param processed_df: Filtered Pandas DataFrame containing target dataset
        :param target: Target label previously passed to 'match_case_dataframe'
        :return:
    """
    matches = len(processed_df)

    if matches <= 1:
        print('{} row returned containing \'{}\''.format(matches, target))
    else:
        print('{} rows returned containing \'{}\''.format(matches, ", ".join(target)))
