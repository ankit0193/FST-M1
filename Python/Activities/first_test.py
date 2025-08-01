import pytest
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert num*num == 40

def testequality():
   assert 10 == 11  



#All test file must be in a 'tests' folder
#All file in the tests folder must start with 'test_' or end with '_test'
#All test functions in the files must start with 'test'   