import unittest
from random import randint
from os import system

class NonDexTest(unittest.TestCase):

    def test_size(self):
        sz = [0, 1, 10]
        for x in sz:
            inorder_keys = []
            d = {}
            for i in range(x):
                d[i] = i
                inorder_keys.append(i)
            ret = list(d.keys())
            if x>=2:
                self.assertNotEqual(inorder_keys, ret)
                #slight probabiilty of still being equal
            ret.sort()
            self.assertEqual(inorder_keys, ret)

    # add more tests for testing over various seeds

    def test_modifications(self):
        # keep this high, so as to reduce chances of identity perm.
        sz = 100

        inorder_keys = []
        d = {}
        for i in range(sz):
            d[i] = i
            inorder_keys.append(i)

        ret = list(d.keys())
        self.assertNotEqual(inorder_keys, ret)
        ret.sort()
        self.assertEqual(inorder_keys, ret)

        for i in range((int)(sz/2)):
            inorder_keys.remove(i)
            d.pop(i, None)
        for i in range((int)(sz/2)):
            inorder_keys.append(i+sz)
            d[i+sz] = i+sz

        # python3 onwards, dict returns keys in the order of addition 
        # (under normal conditions)
        ret = list(d.keys())
        self.assertNotEqual(inorder_keys, ret)
        ret.sort()
        inorder_keys.sort()
        self.assertEqual(inorder_keys, ret)

if __name__ == '__main__':
    unittest.main()
