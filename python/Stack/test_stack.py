import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push("a")
        self.assertEqual(s.size(), 2)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push("a")
        self.assertEqual(s.pop(), "a")
        self.assertEqual(s.pop(), 1)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push("a")
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push("a")
        self.assertEqual(s.size(), 2)

    def test_str(self):
        s = Stack()
        s.push(1)
        s.push("a")
        self.assertEqual(str(s), "Stack is: [1, 'a']")



if __name__ == '__main__':
    unittest.main()

