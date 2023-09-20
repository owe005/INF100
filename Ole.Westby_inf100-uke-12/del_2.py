
def find_item(garden,item):
    # din kode her
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j]==item:
                return (i,j)
    return None

def swap_items(garden1,garden2,pos1,pos2):
    # din kode her
    garden1[pos1[0]][pos1[1]], garden2[pos2[0]][pos2[1]]=garden2[pos2[0]][pos2[1]], garden1[pos1[0]][pos1[1]]
    pass

def clean_garden(my_garden, neighbors_garden):
    """
    Bytt ut all "rock" med "strawberry", og "moss" med "raspberry" fra naboen sin hage
    så lenge det finnes muligheter for bytte.

        Args:
            my_garden - din hage
            neighbors_garden - naboen sin hage
    """
    # din kode her
    for i in range(len(my_garden)):
        for j in range(len(my_garden[i])):
            if my_garden[i][j]=="moss":

                posA = find_item(neighbors_garden,"raspberry")
                if posA != None:
                    swap_items(my_garden,neighbors_garden,(i,j),posA)
            
            if my_garden[i][j]=="rock":
                posA = find_item(neighbors_garden,"strawberry")
                if posA != None:
                    swap_items(my_garden,neighbors_garden,(i,j),posA)
    pass


if __name__ == "__main__":

    my_garden = [
        ["grass", "moss"],
        ["moss", "strawberry"],
        ["moss","rock"]
    ]

    other_garden = [
        ["grass", "raspberry"],
        ["grass", "strawberry"],
        ["strawberry","rock"]
    ]

    clean_garden(my_garden, other_garden)

    my_after = [
        ['grass', 'raspberry'],
        ['moss', 'strawberry'],
        ['moss', 'strawberry']
    ]

    other_after = [
        ['grass', 'moss'],
        ['grass', 'rock'],
        ['strawberry', 'rock']
    ]

    if my_after == my_garden and other_after == other_garden:
        print('OK!')
