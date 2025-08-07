import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable(size=4)

    def test_insert_and_get(self):
        self.table.insert("apple", 10)
        self.assertEqual(self.table.get("apple"), 10)

    def test_update_value(self):
        self.table.insert("test_key", 10)
        self.table.insert("test_key", 20)
        self.assertEqual(self.table.get("test_key"), 20)

    def test_delete(self):
        self.table.insert("banana", 15)
        self.assertTrue(self.table.delete("banana"))
        self.assertIsNone(self.table.get("banana"))

    def test_delete_non_existent_key(self):
        self.assertFalse(self.table.delete("non_existent"))

    def test_collision_handling(self):
        # Force collision by inserting multiple keys that hash to same index
        keys = ["key1", "key2", "key3", "key4"]
        for i, key in enumerate(keys):
            self.table.insert(key, i)

        for i, key in enumerate(keys):
            self.assertEqual(self.table.get(key), i)

    def test_resize(self):
        for i in range(10):  # Trigger resize (load factor > 0.7)
            self.table.insert(f"key{i}", i)

        for i in range(10):
            self.assertEqual(self.table.get(f"key{i}"), i)

        self.assertTrue(self.table.size >= 8)

    def test_count_after_operations(self):
        self.assertEqual(self.table.count, 0)
        self.table.insert("a", 1)
        self.assertEqual(self.table.count, 1)
        self.table.insert("b", 2)
        self.assertEqual(self.table.count, 2)


if __name__ == "__main__":
    unittest.main()