from bs4 import BeautifulSoup
import requests
import json

response=input("Enter the URl to your JEE (Main) April Responses: ")
req=requests.get(response)
response=req.content

key_dict = {}
with open("key.txt") as f:
    for line in f:
        (key, value) = line.split()
        val = [int(e) if e.isdigit() else e for e in value.split(',')]
        key_dict[int(key)] = val

soup = BeautifulSoup(response,'html.parser')

response_data = [[cell.text for cell in row("td")]
                         for row in soup.body.find_all('table', attrs={'class' : 'menu-tbl'})]

count=0
total=0
correct=0
wrong=0
total_correct=0
total_wrong=0



print("Physics:\n")
for x in range(0,30):
	if(response_data[x][15].isdigit()):
		if(int(response_data[x][3 + 2* int(response_data[x][15])]) in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		elif("--5--" in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		else:
			wrong = wrong + 1
		count = count + 1

print("Answered: ", count)
total = total + count
count = 0

print("Correct: ", correct)
print("Wrong: ", wrong)
print("Marks: ", correct * 4 - wrong * 1)

total_correct = total_correct + correct
total_wrong = total_wrong + wrong
correct = 0
wrong=0

print("\n")

print("Chemistry:\n")
for x in range(30,60):
	if(response_data[x][15].isdigit()):
		if(int(response_data[x][3 + 2* int(response_data[x][15])]) in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		elif("--5--" in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		else:
			wrong = wrong + 1
		count = count + 1

print("Answered: ", count)
total = total + count
count = 0

print("Correct: ", correct)
print("Wrong: ", wrong)
print("Marks: ", correct * 4 - wrong * 1)

total_correct = total_correct + correct
total_wrong = total_wrong + wrong
correct = 0
wrong=0

print("\n")

print("Maths:\n")
for x in range(60,90):
	if(response_data[x][15].isdigit()):
		if(int(response_data[x][3 + 2* int(response_data[x][15])]) in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		elif("--5--" in key_dict[int(response_data[x][3])]):
			correct = correct + 1
		else:
			wrong = wrong + 1
		count = count + 1

print("Answered: ", count)
total = total + count
count = 0

print("Correct: ", correct)
print("Wrong: ", wrong)
print("Marks: ", correct * 4 - wrong * 1)

print("\n")

total_correct = total_correct + correct
total_wrong = total_wrong + wrong
correct = 0
wrong=0

print("Total Answered:", total)
print("Total Correct: ", total_correct)
print("Total Wrong:", total_wrong)
print("Total Marks: ", total_correct * 4 - total_wrong * 1)