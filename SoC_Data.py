from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrap_page(url):

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    Project_Name = soup.find('h2', class_ = 'display1 m-3 p-3 text-center project-title')
    #print(f'Project Name: {Project_Name.text}')
    result0 = Project_Name.text
    
    Basic_info = soup.find('div', class_ = 'col-sm-10 col-md-8').find_all('p', class_ = 'lead')
    #print('Mentor Name(s): ')
    result1 = []
    for info in Basic_info:
        if Basic_info.index(info) != len(Basic_info)-1:
            #print(info.text)
            result1.append(info.text)
        
  
    #print('')
    #print(f'No. of Mentees: {Basic_info[-1].text}')
    result2 = Basic_info[-1].text         
    #print('')
    return result0, result1, result2

    '''responses = soup.find_all('p')
    for response in responses:
        if 'Prerequisites' in response.text:
            print(response.text)'''


url = 'https://itc.gymkhana.iitb.ac.in/wncc/soc/'

html_text = requests.get(url).text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
#print(soup)

'''response = soup.find('div', class_ = 'btn-group btn-group-toggle justify-content-center d-flex flex-wrap')
#print(response)

project_fields = response.find_all('label')
for field in project_fields:
    if "Topic" not in field.text and "All" not in field.text:
        print(field.text.strip()) 
        #print('f')'''
    
responses = soup.find_all('div', class_ = 'col-lg-4 col-6 mb-4 shuffle-item')
print(len(responses))

ProjectName = []
Mentor = []
Mentees = []

for response in responses:
    url = response.div.a['href']
    url = 'http://itc.gymkhana.iitb.ac.in' + url
    #print(url)
    result = scrap_page(url)
    ProjectName.append(result[0])
    Mentor.append(result[1])
    Mentees.append(result[2])
    '''print(result[0])
    for i in result[1]:
        print(i)
    print(result[2])    
    print('\n\n')'''
    
'''print(ProjectName)
print(Mentor)
print(Mentees)'''

SOC ={'ProjectName': ProjectName, 'Mentor': Mentor, 'Mentees': Mentees}

df = pd.DataFrame(SOC)
#print(df)

writer = pd.ExcelWriter('SOC_Data.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Sheet1', index = False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

worksheet.set_column('A:A', 50)
worksheet.set_column('B:B', 70)
worksheet.set_column('C:C', 30)

writer._save()