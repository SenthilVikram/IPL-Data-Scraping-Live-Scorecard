import pandas as pd
import re
from bs4 import BeautifulSoup

with open("Doc.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# Deleting a tag and its content because it's a useless tag and interrupts 
# while iterating through player names in table 
for span in soup.find_all("span", {'class':'dismissalSmall'}):
	span.decompose()
for span in soup.find_all("span", {'class':'infoSmall'}): 
	span.decompose() 
	

# CSV filename, Example: "Match 51 - RR vs MI" so that we can store csv file as "Match 51 - RR vs MI.csv"
filename = soup.find(class_=re.compile("matchNav")).get_text()

data = []
for i in soup.find_all(class_=re.compile("teamScorecard")): #iterating through 2 innings
	for tab_i in i.find_all("table"): #iterating through all tables in one innings
		for j in tab_i.find_all("tr"): #iterating through rows in one table
			sub_bat1 = []
			prev_cell = ""
			for sub_elem in j: #iterating through cells in one row (<td>)
				try:
					cell = sub_elem.next_sibling.get_text()
					if cell == "  ": # ignoring useless cell in the table
						continue
					if prev_cell == "Batsmen":
						sub_bat1.append('Dismissal') # filling this blank cell with appropriate name 'Dismissal'
						prev_cell = cell
						continue
					prev_cell = cell #To track the blank cell next to 'Batsmen' cell
					sub_bat1.append(cell) #appending a cell in one row
				except:
					continue
			data.append(sub_bat1) #appending each table

dataFrame = pd.DataFrame(data = data)
# Converting Pandas DataFrame into CSV file
dataFrame.to_csv(f"{filename}.csv")
