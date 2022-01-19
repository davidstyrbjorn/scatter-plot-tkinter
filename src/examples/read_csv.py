
def read_csv():
    import csv
    file = open("D:\Skola\Infovis\\data1.csv")
    reader = csv.reader(file, delimiter = ',')
    data = []
    for idx, row in enumerate(reader):
        data.append((float(row[0]), float(row[1]), str(row[2])))

    min_x = min(data, key = lambda x: x[0])[0]
    max_x = max(data, key = lambda x: x[0])[0]
    min_y = min(data, key = lambda x: x[1])[0]
    max_y = max(data, key = lambda x: x[1])[0]

    return data, min_x, max_x, min_y, max_y


read_csv()
