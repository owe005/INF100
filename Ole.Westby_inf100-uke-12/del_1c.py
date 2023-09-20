import csv

lats1 = []
lons1 = []

lats2 = []
lons2 = []

lats3 = []
lons3 = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2]) # latitude is second last
            lon = float(row[-1]) # longitude is last
        except ValueError:
            continue
        
        if row[20] == "FERSKVANN":
            lats1.append(lat)
            lons1.append(lon)

        if row[20] == "SALTVANN":
            lats2.append(lat)
            lons2.append(lon)
        
        if row[20] == "FERSKVANN/SALTVANN":
            lats3.append(lat)
            lons3.append(lon)
try:
    import matplotlib.pyplot as plt
    plt.plot(lons1,lats1,'+b')
    plt.plot(lons2,lats2,'+r')
    
    #Hvis FERSKVANN/SALTVANN
    plt.plot(lons3,lats3,'+g')

    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats1)} latitudes and {len(lons1)} longitudes')
