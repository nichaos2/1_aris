'''
Created on 9 mai 2019

Used to create a second file to produce the mean values
Supposed that the time marche by 0.1 from the first to the second

This is not used to create additional files but with little efforts it could
However, it is out of the scope of this test

@author: nioannou
'''
import pandas
my_directory = "../resources/"
myfile = 'AIGYM_dataset_example'

def create_second_example_csv():
    #create second dataset
    print('create second file')
    df = pandas.read_csv('../resources/' + myfile + '_1' + '.csv', ';', header=0)
    t_max = df.loc[:,'t'].max();
    df.loc[:,'t']=df.loc[:,'t']+t_max +0.1
    df.loc[1,'Y1']=100
    df2 = df
    print(df2)
    df2.to_csv('../resources/' + myfile + '_2' + '.csv', ';', header=True,index = False)
    
create_second_example_csv()