"""
Docstring for Python_Unittesting
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
"""
import unittest
x="Welcome"
#assert x=="Welcome"
#Returns true
#assert x=="Leave"
#Returns an assertion error

#assert equal
class TestNegative(unittest.TestCase):
    def test_fun(self):
        self.assertEqual("Apples","Lemons","'Apples is not equal to lemons'")
if __name__=='__main__':
    unittest.main()

#Assertisinstance
class Test1:
    x=10
class Test2:
    x=15
class TestClass(unittest.TestCase):
    def test_negative(self):
        objectname=Test1()
        message="They are not the same"
        self.assertIsInstance()