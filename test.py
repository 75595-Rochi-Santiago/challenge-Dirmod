import unittest
import app

class TestOutput(unittest.TestCase):

       def test_output1(self):
              self.assertAlmostEqual(app.calculeSequence("hello world"), "4433555 555666096667775553")
       def test_output2(self):
              self.assertAlmostEqual(app.calculeSequence("hi"), "44 444")
       def test_output3(self):
              self.assertAlmostEqual(app.calculeSequence("yes"), "999337777")

if __name__=="__main__":
       unittest.main()