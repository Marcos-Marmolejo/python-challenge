import os
import csv
sum = 0
sumto = 0
avg = 0
first = 0
second = 0
third = 0
four = 0

# Path to collect data from the Resources folder
bank = os.path.join('pypoll.csv')

with open(bank,'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	#print(csvreader)
	next(csvreader, None)
	for row in csvreader:
		sum= sum+1;
		if row[2]=="Khan":
			first= first+1;
		if row[2]=="Correy":
			second= second+1;
		if row[2]=="Li":
			third= third+1;
		if row[2]=="O'Tooley":
			four= four+1;
		#sumto= sumto + float(row[1]);

#sum = sum -1
print("			-------------------")
print("			-Election Results-")	
print("			-------------------")	
print(f"		Total Votes: {sum}")
print(f"		Khan= {int((first/sum)*100)}% ({first})")
print(f"		Correy= {int((second/sum)*100)}% ({second})")
print(f"		Li= {int((third/sum)*100)}% ({third})")
print(f"		O'Tooley= {int((four/sum)*100)}% ({four})")

if (first>second and first > third and first > four):
	print("				Winner: Khan")
	nombrewin= "khan"
elif (second>first and second > third and second > four):
	print("				Winner: Correy")
	nombrewin= "Correy"
elif (third > first and third > second and third > four):
	print("				Winner: Li")
	nombrewin= "Li"
elif (four > first and four > second and four > third):
	print("				Winner: O'Tooley")
	nombrewin= "O'Tooley"

file = open("TheMonarca.txt","w") 
L = [f"Election Results \n------------------------------ \nTotal Votes: {sum} \nKhan= {int((first/sum)*100)}% ({first})\nCorrey= {int((second/sum)*100)}% ({second})\nLi= {int((third/sum)*100)}% ({third})\nO'Tooley= {int((four/sum)*100)}% ({four})\nWinner: {nombrewin}"]  
file.writelines(L) 
file.close()