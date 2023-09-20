with open('VIK_sealevel_2000.txt') as f:
    mylist = [tuple(i.split(',')) for i in f]

    print(mylist)