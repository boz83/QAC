import pytest
from programs import string_gen

def test_isString():
    assert isinstance(string_gen.string_gen(),str) == True 

def test_length():
    assert len(string_gen.string_gen()) == 5

def test_LowerCase():
    assert str.islower(string_gen.string_gen()) == True