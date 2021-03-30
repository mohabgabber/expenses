import csv #The Csv Writer
import pandas as pd #convert csv to html table
import matplotlib.pyplot as plt #To Create The Visual Plot

#input appears everytime the code is executed

inputmoney = input("Enter The Amount: ")
inputdate  = input("Enter The Date (yyyy/mm/dd): ")
inputdescription = input("Enter The Description: ")
inputshop = input("Enter The Shop: ")

#after the user inputted everything The Code Should Save EvryThing To A CSV File Called expenses.CSV

with open("expenses.csv", "a", newline="\n") as writer:
    csvwriter = csv.writer(writer)
    csvwriter.writerow([inputmoney, inputdate, inputdescription, inputshop])
    writer.close()

#To Create An Html Table Named "Expenses.html"

a = pd.read_csv('expenses.csv')
a.to_html('expenses.html')
html_file = a.to_html()
print(a.head())

#To Print Each Row In A List Of Stirngs

# with open('expenses.csv', 'r') as csv1:
#     csv_reader = csv.reader(csv1)
#     for line in csv_reader:
#         print(line)
# csv1.close()

#To Create A Visual Plot Using pandas And matplotlib
plt.style.use('bmh')
df = pd.read_csv('expenses.csv')
x = df["Amounts"]
y = df['Date']
plt.xlabel('Amounts', fontsize=18)
plt.ylabel('Date', fontsize=18)
plt.bar(x,y)
plt.show()
