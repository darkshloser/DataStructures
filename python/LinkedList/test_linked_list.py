import unittest
from singly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_is_empty_on_init(self):
        self.assertTrue(self.ll.is_empty())

    def test_append_single(self):
        self.ll.append(1)
        self.assertEqual(self.ll.to_list(), [1])

    def test_append_multiple(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])

    def test_prepend(self):
        self.ll.append(2)
        self.ll.prepend(1)
        self.assertEqual(self.ll.to_list(), [1, 2])

    def test_insert_after(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.insert_after(1, 1.5)
        self.assertEqual(self.ll.to_list(), [1, 1.5, 2])

    def test_insert_after_nonexistent(self):
        self.ll.append(1)
        with self.assertRaises(ValueError):
            self.ll.insert_after(99, 5)

    def test_delete_head(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.delete(1)
        self.assertEqual(self.ll.to_list(), [2])

    def test_delete_middle(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.delete(2)
        self.assertEqual(self.ll.to_list(), [1, 3])

    def test_delete_nonexistent(self):
        self.ll.append(1)
        with self.assertRaises(ValueError):
            self.ll.delete(42)

    def test_delete_empty(self):
        with self.assertRaises(ValueError):
            self.ll.delete(1)

    def test_search_found(self):
        self.ll.append(1)
        self.ll.append(2)
        result = self.ll.search(2)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 2)

    def test_search_not_found(self):
        self.ll.append(1)
        self.assertIsNone(self.ll.search(99))

    def test_to_list_empty(self):
        self.assertEqual(self.ll.to_list(), [])

    def test_str_representation(self):
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(str(self.ll), "1 -> 2")


if __name__ == "__main__":
    unittest.main()