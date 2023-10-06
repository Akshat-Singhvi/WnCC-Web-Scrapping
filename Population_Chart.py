from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://worldometers.info/world-population/population-by-country/'

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')
#print(soup)

table = soup.find('table')
#print(table)

Column0 = []
Column1 = []
Column2 = []
Column3 = []
Column5 = []
Column11 = []

rows = table.find_all('tr')

for row in rows:
    if rows.index(row) != 0:
        data = row.find_all('td')
        #print(len(data))
        Column0.append(data[0].text)
        Column1.append(data[1].text)
        Column2.append(data[2].text)
        Column3.append(data[3].text)
        Column5.append(data[5].text)
        Column11.append(data[11].text)

Population_Chart = {'Position': Column0,
                    'Country Name': Column1,
                    'Population': Column2,
                    '% Growth': Column3,
                    'Density': Column5,
                    'World Share': Column11}

df = pd.DataFrame(Population_Chart)
#print(df)

writer = pd.ExcelWriter('Population_Chart.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Table1', index = False)
workbook = writer.book
worksheet = writer.sheets['Table1']

worksheet.set_column('B:B',25)
worksheet.set_column('C:C',15)

writer._save()
