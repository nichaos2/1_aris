'''
Created on 10 mai 2019

Run this to create the file structure you want for the project

The files with the normalised values should be placed in teh resources_norm folder of teh project  
if not change the my_directory

Change the name of the files you want as input and output in constants

Also notice that the location in read and write is hardcoded; you could change that as well

In the end i print the files to see if it is what we want; 
instead of printing you could feed the df straight to your algorithm

@author: nioannou
'''
import os
import numpy as np
import pandas as pd


#
def populate_shift(df, df_shift):
    df_new = pd.concat([df,df_shift.iloc[:,1:]], axis=1)
    return df_new

#
def write_file(df, k):
    df.to_csv('../resources_norm_pop/' + my_norm_pop_file + '_' + str(k) + '.csv', ';', header=True,index = False)

# Constants
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

    # populate
    df_new = df_prot
    for i in range(N):
        #df_shift = df.shift(periods = i+1)            #
        df_shift = df_prot.apply(np.roll,shift=i+1)    # last row goes to first
        df_new = populate_shift(df_new, df_shift)
        
    
    #TODO: delete columns with no use if preferable
    #df_new.iloc[0:1, number_of_cols+1:] = ''
    
    write_file(df_new,k)
    
    # or feed it to wherever you want

