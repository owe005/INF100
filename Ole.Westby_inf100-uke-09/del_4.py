
def max_indexes(xs):
    ix = []
    for i in range(0,len(xs)-2):
        if (xs[i]<xs[i+1]) and (xs[i+1]>xs[i+2]):
            ix.append(i+1)
        elif (xs[i]==xs[i+1]):
            ix.append(i+1)
    return ix


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

# gjerne bruk flere funksjoner

if __name__ == "__main__":
    test = [3, 4, 5, 2, 1, 0, 4, 6, 4, 2, 1]
    if max_indexes(test) == [2,7]:
        print('This works')
    else:
        print("This didn't work")

    test = [2, 3, 3, 1]
    if max_indexes(test) == [2]:
        print('This works')
    else:
        print("This didn't work")

    
    data = read_file("VIK_sealevel_2000.txt")
    
    # use max_indexes to find a list with maximal sea level heights
    # work out the average distance between these maximal heights
    # example:
    #    idxs = max_indexes(heights) # [10,25,40,55,70]
    # Each index is 15 from the next
    # -> average distance 15.0
    # 
    #    idxs = max_indexes(heights) # [3,12,23]
    # The distance between indexes is 9, 11 -> average distance 10.0
