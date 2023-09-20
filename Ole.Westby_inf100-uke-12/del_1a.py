import csv

lats = []
lons = []
arter = {}


with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2]) # latitude is second last
            lon = float(row[-1]) # longitude is last
        except ValueError:
            continue
        if row[12] in arter.keys():
            arter[row[12]] += 1
        else:
            arter[row[12]] = 1
        lats.append(lat)
        lons.append(lon)
        
try:
    import matplotlib.pyplot as plt
    plt.plot(lons,lats,'+')
    plt.show()

    for fisk in arter:
        print(fisk+":"+str(arter[fisk]))

except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
