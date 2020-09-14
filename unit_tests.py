import unittest
from main import MyWindow

class TestSum(unittest.TestCase):
    def test_manipulate_string(self):
        """
        Unit tests
        """
        mywin = MyWindow()
        test_cases = ["Bubble", "abab", "", "DFDDD", "A","Aa"]
        e_out = [['u',"uleBbb"],[None, "aabb"],[None,""],['F',"FDDDD"],['A',"A"],[None,"Aa"]]
        for i in range(0, len(test_cases)):
        	with self.subTest(i=i):
	        	out = mywin.manipulate_string(test_cases[i])
	        	self.assertEqual(out, e_out[i], "Failed Sub Test " + str(i+1))

if __name__ == '__main__':
    unittest.main()