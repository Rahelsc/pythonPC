from prettytable import PrettyTable 


# open csv file 
results_in_csv = open("C:\\Users\\rahel\\Google Drive\\אריאל\\שנה א\\סמסטר ב\\python\\booksSearch.csv", 'r') 

results_in_csv = results_in_csv.readlines() # create a list of the contents

table = PrettyTable()
headers = results_in_csv[0].split(',') # splitting header row to table header
table.field_names = headers # assigning table headers

for row in range(1, len(results_in_csv)):    # traversing array of row to produce table
    table.add_row(results_in_csv[row].split(',')) # splitting rows to list and adding to prettyTable object

html_code = table.get_html_string() # converting to html

html_file = open('C:\\Users\\rahel\\Google Drive\\אריאל\\שנה א\\סמסטר ב\\python\\booksSearch.html', 'w') # creating the html file

html_file = html_file.write(html_code)
