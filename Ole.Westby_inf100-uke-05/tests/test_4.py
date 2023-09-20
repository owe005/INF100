import del_4 as D


def test_pytag_1000():
    assert D.pytag_trippel(1000) == 31875000
    
def test_pytag_204():
    assert D.pytag_trippel(204) == 294780
    
def test_pytag_598():
    assert D.pytag_trippel(598) == 4825860
    
def test_pytag_12():
    assert D.pytag_trippel(12) == 60
    
