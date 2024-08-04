import pandas as pd
import numpy as np
import html5lib
import os

def makeFolder(folderpath):
    if os.path.exists(folderpath):
        return
        #print("Path Exists")
    else:
        os.makedirs(folderpath)
        print("Path does not exist creating....")

def read_from_file(filepath, test=0, n=5, col_Names = [], sheet = 0):
    filetype = filepath.split('.')[1]
    #This will read the csv and display the first 5 rows of the data.
    if (filetype == 'csv'):
        if (col_Names == []):
            dataFrame = pd.read_csv(filepath)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))
        elif (col_Names != []):
            dataFrame = pd.read_csv(filepath, names=col_Names)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))

        return dataFrame

    elif (filetype == 'xlsx'):
        xlFile = pd.ExcelFile(filepath)  
        sheetName = xlFile.sheet_names[sheet]
        dataFrame = xlFile.parse(f'{sheetName}')
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the numbe rof rows.')
        elif (test == 1):
            print(dataFrame.head(n))

        return dataFrame
 
def simple_scraper(url, n=5, test = 0, table_Num = 0, match_term = None):
    #If the url has multiple tables then set the table_Num to get that table
    #The dafault is set to 0 which will display the first one.
    if (match_term == None):
        dataFrame_list = pd.read_html(url)
        dataFrame = dataFrame_list[table_Num]
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
        elif (test == 1):
            print(dataFrame.head(n))
    else:
        dataFrame_list = pd.read_html(url, match=f'{match_term}')
        dataFrame = dataFrame_list[table_Num]
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
        elif (test == 1):
            print(dataFrame.head(n))
    
    return dataFrame

def write_to_csv(dataFrame, destpath, file_name):
    dataFrame.to_csv(f'/{destpath}/{file_name}.csv', mode = 'a', index=False)
    return print('CSV write complete.')

def write_to_xl(dataFrame, destpath, file_name, sheet_name = '1'):
    makeFolder(f'/{destpath}/{file_name}.xlsx')

    return dataFrame.to_excel(f'/{destpath}/{file_name}.xlsx', sheet_name=sheet_name, index=False)

