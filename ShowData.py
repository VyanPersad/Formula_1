import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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

def barPlot(dataFrame, index = None, colNames = None, stacked=False, title='None', xlabel='X-Axis', ylabel='Y-Axis', width=10, height=5):
    #colnames is an array of the column names you wish to plot.
    #the index param is the x axis
    df = dataFrame.dropna()
    df = df[colNames]
    df.set_index(index).plot.bar(rot=0, fontsize = 11, stacked=stacked, figsize=(width,height))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc = (1.04,0.8))
    plt.tight_layout()
    plt.show()

filepath = 'data\locations\Grand_Paris_zone.csv'
colnames = ['Venue','Capacity']

df = read_from_file(filepath)

barPlot(df, index='Venue', colNames=colnames)
