
dict = {}
def make_list():
        global dict
        with open('building_company.csv', 'r', encoding = 'utf - 8') as file:
            lines = file.read().splitlines()
            
            for i in range(len(lines)):
                key = i
                value = []
                value = lines[i].split(';')
                dict.update({key:value})
        return dict    

make_list()
