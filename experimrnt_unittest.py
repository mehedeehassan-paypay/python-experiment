
import unittest
from experiment import TestMe

class TestExperiment(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_as_fuchka(self):
        testme= TestMe()

        self.assertEqual(testme.test2(),11)

    def test_check(self):
        testme= TestMe()

        self.assertEqual(testme.test1(),11)



if __name__=='__main__':
    unittest.main()
