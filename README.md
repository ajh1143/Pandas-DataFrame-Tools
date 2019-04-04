# Pandas DataFrame Tools
Pandas DF related tools for acquisition, parsing, plotting etc
_______________________________________________________________________________________________________________________________________
## Create Custom Data Types    
Generate new categorical data tyoes, option for ordered values. 

```Python3
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
```

_______________________________________________________________________________________________________________________________________
## Sorting Indexes    
Sort indexes of multiindex array. Native solution `sort_index(by='attribute')` currently deprecated. 
```Python3
import pandas as pd
from pandas.api.types import CategoricalDtype

def sort_mixed_dtypes(df, indexes):
    """ Sort indexes in multiindexed dataframe, helpful for multiple custom CategoricalDatatypes
    :DataFrame df: Target dataframe
    :List indexes: Index positions to sort
    :return: DataFrame with sorted index
    """
    return df.reset_index().set_index(indexes).sort_index()
```
## Matching/Filtering
```Python3
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
```
_______________________________________________________________________________________________________________________________________

## Concatenate    
Combine a list of dataframes into single unit, display head and shape. 

```Python3
def concat(df_list):
    df_output = pd.concat(df_list)
    print(df_output.shape)
    print(df_output.head())
    return df_output
```

_______________________________________________________________________________________________________________________________________
## Data Integrity

### Impute NaN With Mean
Replace NaN observations in specified column with mean of populated column
```Python3
def replace_with_mean(df, colname):
    #Generate mean values of specified column
    col_mean = np.mean(df[colname])
    #Add mean values to DataFrame.colname
    df[colname] = df[colname].fillna(col_mean)
    print(df.info())
    return df
```

### Assert Missing
Test if dataframe has missing data via Assert statement
```Python3
def check_missing_data(df):
    #Test assertion of null values
    assert pd.notnull(df).all().all()
```
       

### Remove Duplicate Entries    
Drop duplicates
```Python3
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
```

_______________________________________________________________________________________________________________________________________
## Merge

### Many-To-Many 
```Python3
def merge_many(t1, t2, t3,  t1_left, t2_right, t3_left, tkey_right):
    #Merge T1 and T2 into first_merge table
    first_merge = pd.merge(left=t1, right=t2, left_on=t1_left, right_on=t2_right)
    #Merge first_merge and T3 into second_merge
    second_merge = pd.merge(left=first_merge, right=t3, left_on=t3_left, right_on=tkey_right)
    #Return 3 merged tables into a single table
    return second_merge
```

_______________________________________________________________________________________________________________________________________
## Plotting
### Histogram
```Python3
import pandas as pd
import matplotlib.pyplot as plt

#--------------------
#Function: hist_columns()
#Purpose: Easily generate a Histogram pyplot from a DataFrame and list of columns 
#Inputs: Pandas DataFrame, Log condition(T/F), Rotation value, single or variable column names
#Outputs: Histogram plots of given column in Pandas DataFrame
#--------------------

def hist_columns(df, log, rot, *args):
    # For each column name given, check if log axes chosen, plot histogram
    for arg in args:
        #Check if user passed a logarithmic scale designation
        if log == "True":
            #Create Histogram plot
            df[arg].plot(kind='hist', logx=True, logy=True, rot=rot)
            #Add x-axis label
            plt.xlabel(str(arg))
            #Show plot
            plt.show()
        #No log scale specified
        else:
            #Create Histogram plot
            df[arg].plot(kind='hist', logx=False, logy=False, rot=rot)
            #Add x-axis label
            plt.xlabel(str(arg))
            #Show plot
            plt.show()
```
### Scatter Plot
```Python3
#--------------------
#Purpose: Generate a scatter plot from given datasets 
#Inputs: X-axis data, Y-axis data, X-Axis Label, Y-Axis Label, Graph Title
#Outputs: Populated Scatter Plot with Labels/Title and Legend
#--------------------

def make_scatter(x, y, xlab, ylab, gtitle):
    plt.scatter(x = x, y = y)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(gtitle)
    plt.legend(loc=1)
    plt.grid()
    plt.show()
```

### Time Series Line Plot
```Python3
#--------------------
#Purpose: Generates a TimeSeries Line Plot with labels
#Inputs: Pandas DataFrame, Independent Variable, Dependent Variable, X-Label, Y-Label, Graph Title
#Outputs: TimeSeries LinePlot
#--------------------

def make_timeseries(df, x, y, xlab, ylab, gtitle):
    #Generate a line plot
    df.plot(kind='line', x=x, y=y)
    #Add X&Y axis labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    #Add graph title
    plt.title(gtitle)
    #Add Legend in position 1
    plt.legend(loc=1)
    #Add gridlines to graph
    plt.grid()
    #Show plot
    plt.show()
```

_______________________________________________________________________________________________________________________________________
