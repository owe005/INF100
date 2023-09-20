import del_3 as D

def test_1(capsys):
    D.print_diamond(1)
    output = capsys.readouterr()
    assert output.out.strip('\n') == 'Tall: 1\nX'
    
def test_2(capsys):
    D.print_diamond(2)
    output = capsys.readouterr()
    assert output.out.strip('\n') == 'Tall: 2\n X \nXXX\n X '
    
def test_3(capsys):
    D.print_diamond(3)
    output = capsys.readouterr()
    assert output.out.strip('\n') == 'Tall: 3\n  X  \n XXX \nXXXXX\n XXX \n  X  '
    
def test_4(capsys):
    D.print_diamond(4)
    output = capsys.readouterr()
    assert output.out.strip('\n') == 'Tall: 4\n   X   \n  XXX  \n XXXXX \nXXXXXXX\n XXXXX \n  XXX  \n   X   ', "Diamond 4 failed the test."
    
def test_10(capsys):
    D.print_diamond(10)
    output = capsys.readouterr()
    assert output.out.strip('\n') == 'Tall: 10\n         X         \n        XXX        \n       XXXXX       \n      XXXXXXX      \n     XXXXXXXXX     \n    XXXXXXXXXXX    \n   XXXXXXXXXXXXX   \n  XXXXXXXXXXXXXXX  \n XXXXXXXXXXXXXXXXX \nXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXX \n  XXXXXXXXXXXXXXX  \n   XXXXXXXXXXXXX   \n    XXXXXXXXXXX    \n     XXXXXXXXX     \n      XXXXXXX      \n       XXXXX       \n        XXX        \n         X         ', "Diamond 10 failed the test."
