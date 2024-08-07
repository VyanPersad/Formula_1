import pandas as pd
import numpy as np
import html5lib
import os

def testFunc(dataFrame, test=0, n=5):
    if (test == 0):
        print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
    elif (test == 1):
        print(dataFrame.head(n)) 

def makeFolder(folderpath):
    if os.path.exists(folderpath):
        return print("Path Exists")
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
            test(dataFrame, test, n)

        elif (col_Names != []):
            dataFrame = pd.read_csv(filepath, names=col_Names)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            test(dataFrame, test, n)

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
    #The function has the add parameter of table_num = 'a'
    #If table_num is set to 'a' then what happens is that the function counts 
    #the number of tables on the web page and prints all to a csv
    dataFrame_list = pd.read_html(url)
    if (match_term == None):
        if (table_Num == 'a'):
            print(dataFrame_list)
            dataFrame = pd.concat(dataFrame_list)
            testFunc(dataFrame, test, n)
        elif (table_Num != 'a'):
            dataFrame = dataFrame_list[table_Num]
            testFunc(dataFrame, test, n)
    elif (match_term != None):
        dataFrame_list = pd.read_html(url, match=f'{match_term}')
        dataFrame = pd.concat(dataFrame_list)
        testFunc(dataFrame, test, n)
    
    return dataFrame

def write_to_csv(dataFrame, destpath, file_name):
    dataFrame.to_csv(f'{destpath}/{file_name}.csv', mode = 'a', index=False)
    return print('CSV write complete.')

def write_to_xl(dataFrame, destpath, file_name, sheet_name = '1'):
    folderpath = f'{destpath}/{file_name}.xlsx'
    if os.path.exists(folderpath):
        with pd.ExcelWriter(f'{destpath}/{file_name}.xlsx', engine='openpyxl',mode='a') as writer:
            dataFrame.to_excel(writer, sheet_name, index=False)
        return print("Path Exists")
    else:
        with open(folderpath, 'w') as file:
            print("Path does not exist creating....")
            dataFrame.to_excel(f'{destpath}/{file_name}.xlsx', sheet_name=sheet_name, index=False)
