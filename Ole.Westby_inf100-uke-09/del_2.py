def rename_from_data(filename):
    with open(filename, "r") as line1:
        lines = line1.readlines()

        date = lines[1][:-1] 
        city = lines[0][:-1]
        data = lines[2:]

    

        new_filename = date + "_" + city

        with open(new_filename+".txt", "w+") as output_file:
            for line in data:
                output_file.write(line)
        
def rename_all(namelist):
    for line in namelist:
        rename_from_data(line)

# koden nedover er ikke en del av løsning og 
# brukes ikke i automatisk vurdering. Du kan endre eksemplene eller 
# legge til input() / print() her om du vil, under if __name__...
if __name__ == "__main__": 
    print('Trying to rename...')
    rename_all(['qwghlm.txt', 'qwerty.txt'])
    print('Done.')

    # sjekk på hånd / med editor at 2 nye fil ble lagret med riktig innhold
    
