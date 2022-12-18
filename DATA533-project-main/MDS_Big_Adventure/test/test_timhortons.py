import unittest
import sys 
sys.path.append("..") 
from scene.timhortons import timHortons
from character.alien import alien
from item.food import item

class TestTimhortons(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    
    def setUp(self):
        self.i = item("bacon",20,30,2,2)
        self.i2 = item("potato", 20, 20, 10, 0 )
        self.t = timHortons(0,["plot A","plot B"],alien(0,0,"a",0),[self.i,self.i2])
        
    def test_getInv(self):
        self.assertEqual(self.t.getInv(),[self.i, self.i2])
        self.assertNotEqual(self.t.getInv(),"bread")
        self.assertNotEqual(self.t.getInv(),"milk")
        self.assertNotEqual(self.t.getInv(),20)
    
    def test_checkStock(self):
        self.assertEqual(self.t.checkStock("bacon"), self.i)
        self.assertEqual(self.t.checkStock("skdhg"), 2)
        self.assertEqual(self.t.checkStock("turkey bacon club"), 3)
        self.assertEqual(self.t.checkStock("potato"), 1)
        
    
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

