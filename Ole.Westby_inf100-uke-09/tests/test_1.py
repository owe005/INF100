import del_1 as D

def test_1_name_12():
    assert D.number_name(12) == "twelve"
    
def test_1_name_342():
    assert D.number_name(342) == "three hundred and forty-two"
    
def test_1_name_115():
    assert D.number_name(115) == "one hundred and fifteen"
    
def test_1_name_400():
    assert D.number_name(400) == "four hundred"
    
def test_1_name_100():
    assert D.number_name(100) == "one hundred"
    
def test_1_name_101():
    assert D.number_name(101) == "one hundred and one"
    
def test_1_name_1000():
    assert D.number_name(1000) == "one thousand"
    
def test_1_all_numbernames_5():
    assert D.all_numbernames(5) == 19
    
def test_1_all_numbernames_1():
    assert D.all_numbernames(1) == 3
    
def test_1_all_numbernames_999():
    assert D.all_numbernames(999) == 21113
    
def test_1_euler_17():
    assert D.solve_euler_17() == 21124
