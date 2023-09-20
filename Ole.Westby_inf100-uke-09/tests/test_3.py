import del_3 as D
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

testdata = [
    (2000, 1, 1, 5, 347),
    (2000, 2, 1, 6, 353),
    (2000, 3, 1, 7, 354),
    (2000, 4, 1, 8, 351),
    (2000, 5, 1, 9, 345),
    (2000, 6, 1, 10, 339),
        (2000, 7, 1, 5, 347),
        (2000, 8, 1, 6, 353),
        (2000, 9, 1, 7, 354),
        (2000, 10, 1, 8, 351),
        (2000, 11, 1, 9, 345),
        (2000, 12, 1, 10, 339),
]

def is_close(a, b):
    return abs(a-b) < 0.25


@pytest.fixture(scope="function")
def source_files(tmpdir_factory):
    dir = tmpdir_factory.mktemp("data")
    filename = dir.join("testdata.txt")
    with open(filename,'w') as f:
        for line in testdata:
            f.write(' '.join(map(str, line))+'\n')
    return dir, filename


def test_3_read_big_file():
    data = D.read_file('VIK_sealevel_2000.txt')
    assert len(data) == 8784, f'Expected 8784 lines. Got {len(data)}'
    assert len(data[12]) == 5, f'Expected lines of length 5. Got {len(data[12])}'
    assert type(data[12]) == type(tuple()), f'Expected lines to be tuple. Got {type(data[12])}'
    assert list(map(type,data[12])) == list(map(type,tuple([0,0,0,0,0]))), f'Expected lines to have 5 ints. Got {list(map(type,data[12]))}'
    
def test_3_read_test_file(source_files):
    dir, filename = source_files
    with cwd(dir):
        data = D.read_file(filename)
        assert len(data) == 12, f'Expected 12 lines from test data set. Got {len(data)}'
        assert data == testdata, 'Cannot reproduce test data after read_file'
        assert len(data[4]) == 5, f'Expected lines of length 5. Got {len(data[4])}'
        assert type(data[4]) == type(tuple()), f'Expected lines to be tuple. Got {type(data[4])}'
        assert list(map(type,data[4])) == list(map(type,tuple([0,0,0,0,0]))), f'Expected lines to have 5 ints. Got {list(map(type,data[4]))}'

def test_3_average_big_file():
    data = D.read_file('VIK_sealevel_2000.txt')
    assert len(data) == 8784, f'Expected 8784 lines. Got {len(data)}'
    assert is_close(D.average(data), 347.63763)

def test_3_may_average_big_file():
    data = D.read_file('VIK_sealevel_2000.txt')
    assert len(data) == 8784, f'Expected 8784 lines. Got {len(data)}'
    assert is_close(D.average(data, 5), 337.298387)

def test_3_average_test_data():
    assert is_close(D.average(testdata), 348.166)

def test_3_may_average_test_data():
    assert is_close(D.average(testdata, 5), 345)

def test_3_add_weekday_big_data():
    data = D.read_file('VIK_sealevel_2000.txt')
    assert len(data) == 8784, f'Expected 8784 lines. Got {len(data)}'
    newdata = D.add_weekday(data)
    assert len(newdata) == 8784, f'Expected 8784 lines. Got {len(newdata)}'
    assert len(newdata[12]) == 6, f'Expected lines of length 6. Got {len(newdata[12])}'
    assert type(newdata[12]) == type(tuple()), f'Expected lines to be tuple. Got {type(newdata[12])}'
    assert list(map(type,newdata[12])) == list(map(type,tuple([0,0,0,0,0,'Mon']))), f'Expected lines to have 5 ints and a string. Got {list(map(type,newdata[12]))}'

def test_3_average_weekday_big_data():
    data = D.read_file('VIK_sealevel_2000.txt')
    assert len(data) == 8784, f'Expected 8784 lines. Got {len(data)}'
    newdata = D.add_weekday(data)
    assert len(newdata) == 8784, f'Expected 8784 lines. Got {len(newdata)}'
    
    results = {
        'Sat' : 347.2,
        'Sun' : 347.4,
        'Mon' : 347.1,
        'Tue' : 347.1,
        'Wed' : 348.5,
        'Thu' : 348.6,
        'Fri' : 347.5,
    }
    
    for wd, result in results.items():
        avg = D.average_weekday(newdata, wd)
        assert is_close(avg, result)
