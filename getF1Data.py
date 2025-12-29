from functions import*

dest = 'data/Formula_1_2025'

traskList = ['Australian_Grand_Prix',
'Chinese_Grand_Prix',
'Japanese_Grand_Prix',
'Bahrain_Grand_Prix',
'Saudi_Arabian_Grand_Prix',
'Miami_Grand_Prix',
'Emilia_Romagna_Grand_Prix',
'Monaco_Grand_Prix']

match_term = 'Constructor'
filename = f'Formula_1_Albert'

makeFolder(dest)

for i in traskList:
    urlF1 = f'https://en.wikipedia.org/wiki/2025_{i}'

    df = simple_scraper(urlF1, match_term=match_term)
    write_to_xl(df, dest, file_name=filename, sheet_name=f'{i}')

'''
df = simple_scraper(urlF1, table_Num='a')
print(df)
'''