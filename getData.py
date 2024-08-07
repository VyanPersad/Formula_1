from functions import*
from urls import*

urlArr = [url1,url2,url3,url4,url5,url6,url7,url8,url9]
katieArr = [free40024, free80024, free150024]
names = ['f40024','f80024','f150024']

dest = 'data\katie_ledecky'
file_name = 'katie'

for i in range(3):
    df = simple_scraper(katieArr[i],table_Num='a')
    write_to_csv(df, destpath=dest, file_name=f'{file_name}_{names[i]}')