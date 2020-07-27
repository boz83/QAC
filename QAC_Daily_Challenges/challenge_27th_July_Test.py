import pytest
from challenge_27th_July import sevenNotFive

exampleList = sevenNotFive(1, 36)

def test_one():
  for i in exampleList:
    assert exampleList[i]!='35'
