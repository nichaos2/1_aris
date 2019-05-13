'''
Created on 10 mai 2019

@author: nioannou
'''
import os
import numpy as np
import pandas as pd



def populate_shift(df, df_shift):
    df_new = pd.concat([df,df_shift.iloc[:,1:]], axis=1)
    return df_new

def write_file(df, k):
    df.to_csv('../resources_norm_pop/' + my_norm_pop_file + '_' + str(k) + '.csv', ';', header=True,index = False)


my_norm_file     = 'AIGYM_dataset_example_norm'
my_norm_pop_file = 'AIGYM_dataset_example_norm_pop'

my_directory = "../resources_norm/"
list_of_files = os.listdir(my_directory) # not ordered
number_of_files = len(list_of_files)


#input for N
N = 2

#
for k in range(number_of_files):
    k=k+1
    
    df_prot = pd.read_csv('../resources_norm/' + my_norm_file + '_' + str(k) + '.csv', ';', header=0)

    number_of_rows = df_prot.shape[0]
    number_of_cols = df_prot.shape[1] # 20


# for N=2
# df2 = df_prot.shift(periods = 1)
# df22 = pd.concat([df_prot,df2.iloc[:,1:]], axis=1)
# 
# df2 = df_prot.shift(periods = 2)
# df222 = pd.concat([df22,df_prot.iloc[:,1:]], axis=1)
# 
# #print file
# df222.to_csv('../resources_norm_pop/' + my_norm_pop_file + '_222' + '.csv', ';', header=True,index = False)


    df_new = df_prot
    for i in range(N):
        #df_shift = df.shift(periods = i+1)            #
        df_shift = df_prot.apply(np.roll,shift=i+1)    # last row goes to first
        df_new = populate_shift(df_new, df_shift)
        
    
    #TODO: delete columns with no use if preferable
    write_file(df_new,k)
    
    # or feed it to whereever you want

