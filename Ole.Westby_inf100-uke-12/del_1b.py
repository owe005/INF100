import csv

lats = []
lons = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        if row[12] == "Laks":
         
            try:
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            except ValueError:
                continue
            lats.append(lat)
            lons.append(lon)

try:
    import matplotlib.pyplot as plt
    plt.plot(lons,lats,'+')
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
