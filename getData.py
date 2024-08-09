from functions import*
from urls import*

urlOlympics = 'https://en.wikipedia.org/wiki/1988_Summer_Olympics'
dest = 'data\Delegation_Size'
filename = 'Delegation_Size'
#urlArr = [url10,url11,url12,url13,url14,url15,url16,url17,url18]

match_term = 'Athletes'

#print(simple_scraper(url=urlOlympics, table_Num='a', match_term=match_term))

for i in range(1988,2024,4):
    url = f'https://en.wikipedia.org/wiki/{i}_Summer_Olympics'
    df = simple_scraper(url, table_Num='a', match_term=match_term)
    write_to_xl(df, dest, file_name=filename, sheet_name=f'delSize_{i}')
