import pytest
from challenge_23rd_July import sum 

def test_one():
    for i in range(5):
        assert sum(i) == i + int(str(i)+str(i)) + int(str(i)+str(i)+str(i)) + int(str(i)+str(i)+str(i)+str(i))