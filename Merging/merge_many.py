import pandas as pd

#--------------------
#Language: Python
#Function: merge_many()
#Purpose: Merges multiple tables into a single output tablvia Many-To-Many methodology
#Inputs: Table1, Table2, Table 3, T1 Left, T2 Right, T3 Left, TKey right)
#Outputs: Merged Tables as Single Table
#--------------------

def merge_many(t1, t2, t3,  t1_left, t2_right, t3_left, tkey_right):
    #Merge T1 and T2 into first_merge table
    first_merge = pd.merge(left=t1, right=t2, left_on=t1_left, right_on=t2_right)
    #Merge first_merge and T3 into second_merge
    second_merge = pd.merge(left=first_merge, right=t3, left_on=t3_left, right_on=tkey_right)
    #Return 3 merged tables into a single table
    return second_merge
