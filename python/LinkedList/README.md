# Singly Linked List in Python

This module provides a simple implementation of a **Singly Linked List** in Python using `Node` and `LinkedList` classes. It supports typical linked list operations like `append`, `prepend`, `insert_after`, `delete`, and `search`.

---

## Classes

### `Node`

A class representing a single node in the linked list.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

## Methods and Time Complexities

| Method                            | Description                                  | Time Complexity |
| --------------------------------- | -------------------------------------------- | --------------- |
| `is_empty()`                      | Check if the list is empty                   | O(1)            |
| `append(value)`                   | Add a node to the end of the list            | O(n)            |
| `prepend(value)`                  | Add a node to the beginning of the list      | O(1)            |
| `insert_after(prev_value, value)` | Insert after a node with a specific value    | O(n)            |
| `delete(value)`                   | Delete the first node that matches the value | O(n)            |
| `search(value)`                   | Search for a node by its value               | O(n)            |
| `to_list()`                       | Convert the linked list to a Python list     | O(n)            |
| `__str__()`                       | String representation of the linked list     | O(n)            |

## Usage Example

```python
if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    print(ll)  # Output: 0 -> 1 -> 2

    ll.insert_after(1, 1.5)
    print(ll)  # Output: 0 -> 1 -> 1.5 -> 2

    ll.delete(0)
    print(ll)  # Output: 1 -> 1.5 -> 2

    found_node = ll.search(2)
    print("Search 2:", found_node.value if found_node else "Not found")  # 2

    print("Search 99:", ll.search(99))  # None
```

[⬅ Back to Root README](../../README.md)
