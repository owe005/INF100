with open("qwghlm.txt", "r") as line1:
    lines = line1.readlines()

    date = lines[1][:-1] 
    city = lines[0][:-1]
    data = lines[2:]

    new_filename = date + "_" + city
    print(new_filename)

with open(new_filename+".txt", "w+") as output_file:
    for line in data:
        output_file.write(line)