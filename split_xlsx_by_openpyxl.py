import openpyxl
import csv

book = openpyxl.load_workbook('a.xlsx')
sheet = book.active

of = open('a.csv', 'w')
for i in range(1, 177):
	line = sheet['A%d'%i].value
	new_line = line.replace('\t', ',')
	of.write(new_line+'\n')
	

of.close()
