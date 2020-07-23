import pytest
import challenge_22nd_July as ch
import random

exampleList = str(random.sample(range(20, 40), 5))


def test_string():
  assert type(ch.function(exampleList)) is str #checks output is string data type

def test_formatting():
  assert ch.function("hello world and practice 22 makes perfect and 98 hello world again") == "22 98 again and hello makes perfect practice world"