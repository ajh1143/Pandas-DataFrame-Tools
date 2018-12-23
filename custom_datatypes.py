import pandas as pd
from pandas.api.types import CategoricalDtype

def sort_mixed_dtypes(df, indexes):
    """ Sort indexes in multiindexed dataframe, helpful for multiple custom CategoricalDatatypes
    :DataFrame df: Target dataframe
    :List indexes: Index positions to sort
    :return: DataFrame with sorted index
    """
    return df.reset_index().set_index(indexes).sort_index()


def categorical_datatype(levels, ordered):
    """ Create new categorical datatype
    :param levels: Category Levels, list/tuple form.
    :param ordered: Boolean choice, determeines if input list is in hierarchical order of entry.
    :return: New categorical datatype w/ levels and ordering choice.
    """
    if isinstance(type(levels), list):
        category_name = CategoricalDtype(levels, ordered=ordered)
        return category_name
    else:
        try:
            levels = list(levels)
        except ValueError:
            print("Please enter a valid, non-empty data structure, list/tuple of levels")
        else:
            category_name = CategoricalDtype(levels, ordered=ordered)
            return category_name
