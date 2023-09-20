import del_4 as D

def test_4_maxindex_A():
    assert D.max_indexes([3, 4, 5, 2, 1, 0, 4, 6, 4, 2, 1]) == [2, 7]

def test_4_maxindex_B():
    assert D.max_indexes([2, 3, 3, 1]) == [2]

def test_4_maxindex_252():
    assert D.max_indexes([2, 5, 2]) == [1]

def test_4_maxindex_25252525252():
    assert D.max_indexes([2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2]) == [1,3,5,7,9]
    
def test_4_maxindex_000010():
    assert D.max_indexes([0,0,0,0,1,0]) == [4]
