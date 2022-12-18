import unittest
import sys 
sys.path.append("..") 
from item.food import item

class TestItem(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.i = item("bacon",20,30,2,2)
        
    def test_gethp(self):
        self.assertEqual(self.i.gethp(),20)
        self.assertNotEqual(self.i.gethp(),"bacon")
        self.assertNotEqual(self.i.gethp(),30)
        self.assertNotEqual(self.i.gethp(),2)
        
    def test_getprice(self):
        self.assertEqual(self.i.getprice(),2)
        self.assertNotEqual(self.i.getprice(),200)
        self.assertNotEqual(self.i.getprice(),-1)
        self.assertNotEqual(self.i.getprice(),100)
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

