from functions import*

dest = 'data/Formula_1'

'''match_term = 'Albert'''
filename = f'Formula_1_Albert'

makeFolder(dest)

'''
for i in range(2000,2025,1):
    urlF1 = f'https://en.wikipedia.org/wiki/{i}_Formula_One_World_Championship'

    df = simple_scraper(urlF1, table_Num='a', match_term = match_term)
    write_to_xl(df, dest, file_name=filename, sheet_name=f'form_1_{i}')
    print(i)
'''
urlF1 = f'https://www.formula1.com/en/results/2025/races/1254/australia/qualifying'

df = simple_scraper(urlF1, table_Num='a')
write_to_xl(df, dest, file_name=filename, sheet_name=f'qualifying')

'''
df = simple_scraper(urlF1, table_Num='a')
print(df)
'''