import del_1 as D


def test_A():
    assert D.complement('A') == 'T'

def test_T():
    assert D.complement('T') == 'A'

def test_G():
    assert D.complement('G') == 'C'

def test_C():
    assert D.complement('C') == 'G'

def test_ATAGCAGT():
    assert D.complement("ATAGCAGT") == "ACTGCTAT"
    
def test_ATAGCAGTGGGGCCCC():
    assert D.complement("ATAGCAGTGGGGCCCC") == "GGGGCCCCACTGCTAT"
        
def test_id_1():
    assert D.complement(D.complement("ACT")) == "ACT"
    
def test_id_2():
    assert D.complement(D.complement("TTTTTTT")) == "TTTTTTT"

def test_id_3():
    assert D.complement(D.complement("CGATGCTAGTCGTATGC")) == "CGATGCTAGTCGTATGC"
