import matplotlib.pyplot as plt
def dummy(*args,**kwargs): print(f'Dummy: {args} {kwargs}.'); return 0
plt.show = dummy

def test_import_1a():
    import del_1a

def test_import_1b():
    import del_1b

def test_import_1c():
    import del_1c

def test_import_1d():
    import del_1d
