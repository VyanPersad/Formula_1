import pandas as pd


'''Venues'''

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
    return dataFrame.to_csv(f'{destpath}/{file_name}.csv', mode='a', index=False, header=False)

'''
venuRL = 'https://en.wikipedia.org/wiki/2024_Summer_Olympics'
label = ['Grand Paris zone','Paris Centre zone','Versailles zone','Outlying venues','Non-competitive']

for i in range(5):
    df = simple_scraper(venuRL, test=1, table_Num=(i+4))
    label_row = {label[i]}
    df_row = pd.DataFrame([label_row])
    write_to_csv(df_row, 'data', 'allTables')
    write_to_csv(df, 'data', 'allTables')
'''

archURL = 'https://en.wikipedia.org/wiki/Archery_at_the_2024_Summer_Olympics_%E2%80%93_Women%27s_team'

df = simple_scraper(archURL, n=5, test=1, table_Num=7)
write_to_csv(df, 'data/archery', 'archWomensRank')