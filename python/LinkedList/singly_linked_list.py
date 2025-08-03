
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, value):
        """Add a node at the end."""
        node = Node(value)
        if self.is_empty():
            self.head = node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def prepend(self, value):
        """Add node at the beginning """
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_after(self, prev_value, value):
        """Insert after node with specific value"""
        current = self.head
        while current:
            if current.value == prev_value:
                node = Node(value)
                node.next = current.next
                current.next = node
                return 
            current = current.next
        raise ValueError(f"Value {prev_value} not found in the list.")
    
    def delete(self, value):
        """Delete the first node which match the value"""
        if self.is_empty():
            raise ValueError("List is empty.")
        prev = self.head
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return             
            prev, current = current, current.next
        raise ValueError(f"Value {value} was not found.")
    
    def search(self, value):
        """Search node by specific value"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return

    def to_list(self):
        """Convert Linked List to a Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(v) for v in self.to_list()) or "Empty"
    

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.prepend(0)
#     print(ll)  # 0 -> 1 -> 2

#     ll.insert_after(1, 1.5)
#     print(ll)  # 0 -> 1 -> 1.5 -> 2

#     ll.delete(0)
#     print(ll)  # 1 -> 1.5 -> 2

#     print("Search 2:", ll.search(2))     # Node  
#     print("Search 99:", ll.search(99))   # None