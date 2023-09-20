import del_2 as D
import pytest
from random import randint
import os

from contextlib import contextmanager

@contextmanager
def cwd(path):
    oldpwd=os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


@pytest.fixture(scope="function")
def source_files(tmpdir_factory):
    dir = tmpdir_factory.mktemp("data")
    fns = [
        dir.join("foo.txt"),
        dir.join("bar.txt"),
        dir.join("baz.txt"),
    ]
    with open(fns[0],'w') as f0, open(fns[1],'w') as f1, open(fns[2],'w') as f2:
        f0.write("Eren\n2035-03-30\n")
        f1.write("Mikasa\n2035-02-10\n")
        f2.write("Armin\n2035-11-03\n")
    
        for f in [f0,f1,f2]:
            for _ in range(10):
                f.write(f'{randint(0,100)} {randint(0,100)} {randint(0,100)} {randint(0,100)}\n')
    
    return dir, fns


# contents of test_image.py
def test_2_rename_from_data(source_files):
    dir, fns = source_files
    
    with cwd(dir):
        before = set(os.listdir(dir))
        D.rename_from_data(str(fns[0]))
        after = set(os.listdir(dir))
        assert len(after) == len(before) + 1, f"You haven't created the right number of files: {len(after)-len(before)} instead of 1"
        expected = set(['2035-03-30_Eren.txt'])
        assert after - before == expected, f"Your file has the wrong name: '{after-before}' instead of {expected}"
        
        
def test_2_rename_all(source_files):
    dir, fns = source_files
    
    with cwd(dir):
        before = set(os.listdir(dir))
        D.rename_all(map(str,fns))
        after = set(os.listdir(dir))
        assert len(after) == len(before) + 3, f"You haven't created the right number of files: {len(after)-len(before)} instead of 3"
        expected = set(['2035-03-30_Eren.txt','2035-02-10_Mikasa.txt','2035-11-03_Armin.txt'])
        assert after - before == expected, f"Your files have the wrong names: '{after-before}' instead of {expected}"
        
        
def test_2_content(source_files):
    dir, fns = source_files
    
    with cwd(dir):
        D.rename_all(map(str,fns))
        pairs = [
            ('foo.txt','2035-03-30_Eren.txt'),
            ('bar.txt','2035-02-10_Mikasa.txt'),
            ('baz.txt','2035-11-03_Armin.txt'),
        ]
        for before, after in pairs:
            with open(before) as bf, open(after) as af:
                blines = bf.readlines()
                alines = af.readlines()
                
            for i, (a, b) in enumerate(zip(alines, blines[2:])): # skip the 2 info lines
                assert a == b, f'Mismatch in data line {i+1} of {before}/{after}: {a.strip()} != {b.strip()}'
