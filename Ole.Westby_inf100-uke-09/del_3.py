def read_file(filename):
    data=[]
    with open(filename, "rt") as f:
        data = f.readlines()
        for row in range(len(data)):
            data[row] = list(data[row].split())
        for row in range(len(data)):
            for col in range(len(data[row])):
                data[row][col]=int(data[row][col])
            data[row]=tuple(data[row])
    return data

def average(data, month=None):
    sum = 0
    d = 0

    if month == None:
        for row in data:
            sum += row[len(row)-1]
        return sum/len(data)
    else:
        for row in data:
            if month == row[1]:
                sum += row[len(row)-1]
                d+=1
        return sum/d

def add_weekday(data):        
    weekday = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
    Fir = weekday[0]
    Last = weekday[1]

    data2 = []
    day = 0
    for row in range(len(data)-1):
        now = data[row][2]
        next = data[row+1][2]

        if next == now:
            data[row] = list(data[row])
            data[row].append(weekday[day])
            data[row]=tuple(data[row])
        else:
            data[row] = list(data[row])
            data[row].append(weekday[day])
            data[row] = tuple(data[row])
            if day < 6:
                day=day+1
            else: 
                day=0
    else:
        data[len(data)-1]=list(data[len(data)-1])
        data[len(data)-1].append(weekday[day])
        data[len(data)-1]=tuple(data[len(data)-1])

    return data
    
def average_weekday(data, wkd):
    sum = 0
    r = 0
    for row in data:
        if row[len(row)-1] == wkd:
            sum+=row[len(row)-2]
            r+=1
    return sum/r


if __name__ == "__main__":
    
    data = read_file("VIK_sealevel_2000.txt")
    print(data[:5])
    
    annual_avg = average(data)
    print('Annual average:',annual_avg,'cm')
    
    july_average = average(data, 7)
    print('July average:',july_average,'cm')
    
    for month in range(1,13):
        print(f'{month:2} average is {average(data, month):5.1f} cm')
        
    data_2 = add_weekday(data)
    print(data_2[:25])

    for wd in ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']:
        avg = average_weekday(data_2, wd)
        print(f'{wd}: {avg:5.1f} cm.')
        
