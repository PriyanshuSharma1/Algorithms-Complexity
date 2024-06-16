import unittest
from dynamic import knapsack

class TestFractionalKnapsack(unittest.TestCase):
    def test_knapsack(self):
        weights=[20,30,15,40]
        values=[100,120,60,90]
        capacity=50
        maxvalue=knapsack(weights,values,capacity)
        self.assertAlmostEqual(maxvalue,220)
    
    def test_knapsack_empty(self):
        weights=[]
        values=[]
        capacity=50
        maxvalue=knapsack(weights,values,capacity)
        self.assertAlmostEqual(maxvalue,0)

    def test_knapsack_zero_capacity(self):
        weights=[20,30,15,40]
        values=[100,120,60,90]
        capacity=0
        maxvalue=knapsack(weights,values,capacity)
        self.assertAlmostEqual(maxvalue,0)

    def test_knapsack_all_items(self):
        weights=[10,20,30,40]
        values=[60,100,120,150]
        capacity=100
        maxvalue=knapsack(weights,values,capacity)
        self.assertAlmostEqual(maxvalue,430) 

if __name__=='__main__':
    unittest.main()