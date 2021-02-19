import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        n1 = Node(10)
        n2 = Node(20)
        self.assertEqual(n1<n2, True)

    def test_simple_02(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(10)
        t_list.add(3)
        t_list.add(7)
        self.assertEqual(t_list.python_list(), [3,5,7,10])
        self.assertEqual(t_list.index(5), 1)
        self.assertEqual(t_list.index(6), None)
        self.assertEqual(t_list.python_list_reversed(), [10, 7, 5, 3])
        self.assertTrue(t_list.remove(7))
        self.assertTrue(t_list.remove(3))

    def test_simple_03(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(10))
        self.assertEqual(t_list.index(10), None)
        self.assertEqual(t_list.size(), 0)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        self.assertFalse(t_list.search(10))
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        self.assertFalse(t_list.search(10))
        self.assertEqual(t_list.size(), 0)
        t_list.add(20)
        self.assertEqual(t_list.size(), 1)


if __name__ == '__main__': 
    unittest.main()
