filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}.txt"
    print(row)

