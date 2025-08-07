
class HashTableEntry:
    # Purpose: Holds one Key <-> Value pair
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.is_active = True  # Flag if entry is present or it was deleted


class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.count = 0
        self.table = [None] * size

    def _hash(self, key, attempt):
        return (hash(key) + attempt) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.count = 0
        self.table = [None] * self.size

        for entry in old_table:
            if entry and entry.is_active:
                self.insert(entry.key, entry.value)

    def insert(self, key, value):
        if self.count / self.size > 0.7:
            self._resize()

        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            entry = self.table[idx]

            if entry is None or not entry.is_active or entry.key == key:
                self.table[idx] = HashTableEntry(key, value)
                self.count += 1
                return
            attempt += 1
        raise RuntimeError("Hash table is full")

    def get(self, key):
        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            entry = self.table[idx]
            if entry is None:
                return None
            if entry.is_active and entry.key == key:
                return entry.value
            attempt += 1
        return None

    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            entry = self.table[idx]
            if entry is None:
                return False
            if entry.is_active and entry.key == key:
                entry.is_active = False
                self.count -= 1
                return True
            attempt += 1
        return False

ht = HashTable()

ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("orange", 7)

print(ht.get("banana"))  # Output: 3

ht.delete("banana")
print(ht.get("banana"))  # Output: None