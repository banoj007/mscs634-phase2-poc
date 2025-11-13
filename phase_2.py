

# --------------------------
# 1. TRIE DATA STRUCTURE
# --------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# --------------------------
# 2. MIN HEAP DATA STRUCTURE
# --------------------------

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None


# --------------------------
# 3. HASH TABLE IMPLEMENTATION
# --------------------------

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# --------------------------
# 4. DEMONSTRATION / TEST CASES
# --------------------------

if __name__ == "__main__":
    print("=== Proof of Concept: Data Structures Implementation ===")

    # ---- Trie Demo ----
    print("\n--- Trie Demo ---")
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    print("Search 'apple':", trie.search("apple"))
    print("Search 'appl':", trie.search("appl"))
    print("Starts with 'ban':", trie.starts_with("ban"))

    # ---- Min Heap Demo ----
    print("\n--- Min Heap Demo ---")
    heap = MinHeap()
    for num in [5, 3, 8, 1, 2]:
        heap.insert(num)
        print("Inserted:", num, "Heap:", heap.heap)
    print("Extract Min:", heap.extract_min())
    print("Heap after extract:", heap.heap)
    print("Current Min:", heap.get_min())

    # ---- Hash Table Demo ----
    print("\n--- Hash Table Demo ---")
    hash_table = HashTable()
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 25)
    hash_table.insert("city", "New York")
    hash_table.display()
    print("Search 'age':", hash_table.search("age"))
    hash_table.delete("city")
    print("After deleting 'city':")
    hash_table.display()

