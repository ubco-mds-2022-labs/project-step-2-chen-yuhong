import unittest
import sys 
sys.path.append("..") 
from character.character import character

class TestCharacter(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.c = character(100,50)
        
    def test_fight(self):
        self.assertEqual(self.c.fight(),50)
        self.assertNotEqual(self.c.fight(),100)
        self.assertNotEqual(self.c.fight(),0)
        self.assertNotEqual(self.c.fight(),-100)
        
    def test_display(self):
        self.assertEqual(self.c.display(),"Health: 100 power: 50")
        self.assertNotEqual(self.c.display(),"Health: 100 power: 100")
        self.assertNotEqual(self.c.display(),"power: 50")
        self.assertNotEqual(self.c.display(),"100; 50")
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   
