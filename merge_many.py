import pandas as pd

#Merges multiple tables in a many-to-many methodology
def merge_many(t1, t2, t3,  t1_left, t2_right, t3_left, tkey_right):
    first_merge = pd.merge(left=t1, right=t2, left_on=t1_left, right_on=t2_right)
    second_merge = pd.merge(left=first_merge, right=t3, left_on=t3_left, right_on=tkey_right)
    return second_merge
