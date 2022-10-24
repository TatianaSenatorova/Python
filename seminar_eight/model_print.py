

def print_table():
    with open('building_company.csv', 'r', encoding = 'utf - 8') as file:
        for line in file:
            print(line)
 
print_table()      
