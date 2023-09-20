
def test_find():
    import del_2 as M
    
    test_garden = [
        ["moss", "strawberry"],
        ["moss","rock"],
        ["grass", "moss"],
    ]
    
    pos = M.find_item(test_garden, "rock")
    assert pos == (1,1)
    
    pos = M.find_item(test_garden, "grass")
    assert pos == (2,0)
    
    pos = M.find_item(test_garden, "raspberry")
    assert pos == None
    

def test_swap():
    import del_2 as M
    a = [["moss","raspberry"]]
    b = [["rock","grass"]]
    M.swap_items(a,b,(0,0),(0,1))
    assert a == [["grass","raspberry"]]
    assert b == [["rock","moss"]]


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

def test_clean_garden_good_stuff_in_my_garden():
    import del_2 as M

    my = [ row[:] for row in my_garden ]
    other = [ row[:] for row in other_garden ]

    M.clean_garden(my, other)

    assert my_after == my

def test_clean_garden_bad_stuff_in_neighbors_garden():
    import del_2 as M

    my = [ row[:] for row in my_garden ]
    other = [ row[:] for row in other_garden ]

    M.clean_garden(my, other)

    assert other == other_after
