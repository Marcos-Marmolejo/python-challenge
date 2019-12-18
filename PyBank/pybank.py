import os
import csv
sum = 0
sumto = 0
avg = 0
Maximo = 0
Minimo = 0
resta = 0
appenddata=[]
pivot= 0
# Path to collect data from the Resources folder
bank = os.path.join('PyBank_D.csv')

with open(bank,'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	#print(csvreader)
	next(csvreader, None)
	for row in csvreader:
		appenddata.append(row)
		sum= sum+1;
		sumto= sumto + float(row[1]);

	for i in range(len(appenddata)-1):
		resta = float(appenddata[i+1][1]) - float(appenddata[i][1])
		pivot = resta + pivot
		if resta > Maximo:
			Maximo = resta
			nombre = appenddata[i+1][0]
		if resta < Minimo:
			Minimo = resta
			nombre2 = appenddata[i+1][0]
		#print(row)
#sum = sum -1
avg = pivot/(sum-1)
print("Financial Analysis")		
print(f"Total months: {sum}")
print(f"total= {sumto}")
print(f"avg= {avg}")
print(f"Greatest Increase in Profits: {nombre} : (${Maximo})")
print(f"El valor minimo es el numero: {nombre2} : (${Minimo})")   