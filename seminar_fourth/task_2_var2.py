a = "2*x**2 + 4*x + 2"
transformed = a.replace('*x**2', ' ').replace('*x', ' ').replace('+ ', ' ').replace('- ', ' ')
print(transformed)
lst = transformed.split(' ')
abc = []
for item in lst:
    try:
        num = float(item)
        abc.append(num)
    except:
        continue  
print(abc)
a, b, c = 0, 0, 0
