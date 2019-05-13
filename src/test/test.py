'''
Created on 9 mai 2019
Edited on 13 mai 2019

Run this to create files with normalised values 

the files should be placed in the folder resources in the project
if not change the my_directory

Change the name of the files you want as input and output in constants

Also notice that the location in read and write is hardcoded; you could change that as well

@author: nioannou
'''

import os
import numpy
import pandas

#constants
my_directory = "../resources/"
myfile = 'AIGYM_dataset_example'
mynewfile = 'AIGYM_dataset_example_norm'

list_of_files = os.listdir(my_directory) # not ordered
number_of_files = len(list_of_files)

# define min max dictionaries
max=dict()
max['t']=0
min=dict()
min['t']=0


def find_col_max(df, col):
    if col!='t':
        return df.loc[:,col].max();
    else:
        return 0
def find_col_min(df, col):
    if col!='t':
        return df.loc[:,col].min();
    else:
        return 0

def find_min_max():
    #read files
    print('read csv files')
    for i in range(number_of_files):
        i=i+1
        df = pandas.read_csv('../resources/' + myfile + '_' + str(i) + '.csv', ';', header=0)
        
        number_of_rows = df.shape[0]
        number_of_cols = df.shape[1]
        
        
        #find the min and max of every column
        for col in list(df.columns): 
            new_max = find_col_max(df, col)
            new_min = find_col_min(df, col)
            
            
            #create dict the first time
            if i==1:
                max[col]=new_max
                min[col]=new_min
            
            #compare with later csv's
            if new_max>max[col]:
                max[col]=new_max
            if new_min<min[col]:
                min[col]=new_min
            
    return (min, max)

def normalize():
    '''
    normalise all the values 
    x_norm = (x - x_min) / (x_max-x_min)
    
    now we create files with the normalised values, but it is not the best idea
    when I understand the end product it will be better not to create the new files but to feed the output directly to the learning algorithm
    
    TODO: create the folder resources_norm if it does not exist
    '''

    for i in range(number_of_files):
        i=i+1
        df = pandas.read_csv('../resources/' + myfile + '_' + str(i) + '.csv', ';', header=0)
        df2=df
        for col in list(df.columns):
            if col!='t':
                df2[col]= (df[col]-min[col])/(max[col] - min[col])
        df2.to_csv('../resources_norm/' + mynewfile + '_' + str(i)+ '.csv', ';', header=True,index = False)
        
        
min = find_min_max()[0]
max = find_min_max()[1]

normalize()

