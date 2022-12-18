import unittest
import sys 
sys.path.append("..") 
from character.player import player

class TestPlayer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.p = player(100,50,0,1)
        
    def test_showMoney(self):
        self.assertEqual(self.p.showMoney(),0)
        self.assertNotEqual(self.p.showMoney(),100)
        self.assertNotEqual(self.p.showMoney(),50)
        self.assertNotEqual(self.p.showMoney(),-100)
        
    def test_getidentity(self):
        self.assertEqual(self.p.getidentity(),1)
        self.assertNotEqual(self.p.getidentity(),0)
        self.assertNotEqual(self.p.getidentity(),2)
        self.assertNotEqual(self.p.getidentity(),3)
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

