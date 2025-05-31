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
print("Choose mode:\n1 key value  --> put\n2 key        --> get\n3            --> print cache")

for _ in range(n):
    parts = input().strip().split()
    if not parts:
        continue
    mode = int(parts[0])
    if mode == 1:
        key = int(parts[1])
        value = int(parts[2])
        lru.put(key, value)
    elif mode == 2:
        key = int(parts[1])
        print(lru.get(key))
    elif mode == 3:
        lru.print_cache()
    else:
        print("Invalid mode.")
