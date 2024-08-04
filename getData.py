from functions import*

url1 = 'https://en.wikipedia.org/wiki/1988_Summer_Olympics_medal_table'
url2 = 'https://en.wikipedia.org/wiki/1992_Summer_Olympics_medal_table'
url3 = 'https://en.wikipedia.org/wiki/1996_Summer_Olympics_medal_table'
url4 = 'https://en.wikipedia.org/wiki/2000_Summer_Olympics_medal_table'
url5 = 'https://en.wikipedia.org/wiki/2004_Summer_Olympics_medal_table'
url6 = 'https://en.wikipedia.org/wiki/2008_Summer_Olympics_medal_table'
url7 = 'https://en.wikipedia.org/wiki/2012_Summer_Olympics_medal_table'
url8 = 'https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table'
url9 = 'https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table'

urlArr = [url1,url2,url3,url4,url5,url6,url7,url8,url9]

dest = 'data/olympics'
file_name = 'MedalRanks'

for i in range(1988, 2024, 4):
    url = f'https://en.wikipedia.org/wiki/{i}_Summer_Olympics_medal_table'
    df = simple_scraper(url, test=0, match_term='Rank')
    #write_to_csv(df, destpath=dest,file_name=f'{file_name}_{i}')
    sheet_name=f'Medals_{i}'
    print(sheet_name)
    write_to_xl(df, destpath=dest, file_name=file_name, sheet_name=sheet_name)