import del_2 as D

def test_10(capsys):
    D.print_prime_factors(10)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 10\n2\n5'
    
def test_27(capsys):
    D.print_prime_factors(27)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 27\n3\n3\n3'
    
def test_28(capsys):
    D.print_prime_factors(28)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 28\n2\n2\n7'
    
def test_53(capsys):
    D.print_prime_factors(53)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 53\n53'
    
def test_14092020(capsys):
    D.print_prime_factors(14092020)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 14092020\n2\n2\n3\n3\n5\n79\n991'

def test_101(capsys):
    D.print_prime_factors(101)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 101\n101'

def test_48(capsys):
    D.print_prime_factors(48)
    output = capsys.readouterr()
    assert output.out.strip() == 'Input: 48\n2\n2\n2\n2\n3'
