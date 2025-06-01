class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self._insert_at_front(new_node)
        self.cache[key] = new_node

    def print_cache(self):
        cur = self.head.next
        result = []
        while cur != self.tail:
            result.append(f"{cur.key}:{cur.value}")
            cur = cur.next
        print("Cache [Most -> Least Recent]:", " -> ".join(result))


# ------- Driver code --------
capacity = int(input("Enter capacity of LRU Cache: "))
lru = LRUCache(capacity)

n = int(input("Enter number of operations: "))

for i in range(n):
    print(f"\nOperation {i+1}:")
    print("Select operation:")
    print("1 - Put")
    print("2 - Get")
    print("3 - Print Cache")
    
    try:
        op = int(input("Enter choice (1/2/3): ").strip())
    except ValueError:
        print("Invalid input. Skipping operation.")
        continue

    if op == 1:
        try:
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            lru.put(key, value)
        except ValueError:
            print("Invalid key or value.")
    elif op == 2:
        try:
            key = int(input("Enter key: "))
            result = lru.get(key)
            print(f"Value: {result}")
        except ValueError:
            print("Invalid key.")
    elif op == 3:
        lru.print_cache()
    else:
        print("Invalid operation.")
