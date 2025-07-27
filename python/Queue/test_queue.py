import unittest
from collections import deque
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue_and_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        q.enqueue("d")
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), "a")
        self.assertEqual(q.dequeue(), "b")
        self.assertEqual(q.dequeue(), "c")
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), "d")
        self.assertTrue(q.is_empty())

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue("a")
        self.assertFalse(q.is_empty())
        q.enqueue("b")
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue("a")
        q.enqueue("b")
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)

    def test_dequeue_empty_raises(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_str(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        print(str(q))
        self.assertEqual(str(q), "Queue is: ['a', 'b']")

if __name__ == '__main__':
    unittest.main()

