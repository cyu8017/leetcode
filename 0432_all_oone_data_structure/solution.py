# LeetCode 0432 - All O`one` Data Structure
# https://leetcode.com/problems/all-oone-data-structure/


class Node:
    __slots__ = ("count", "keys", "prev", "next")

    def __init__(self, count: int = 0):
        self.count = count
        self.keys: set[str] = set()
        self.prev: Node | None = None
        self.next: Node | None = None


class AllOne:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_nodes: dict[str, Node] = {}

    def _insert_after(self, anchor: Node, node: Node) -> None:
        node.prev = anchor
        node.next = anchor.next
        anchor.next.prev = node
        anchor.next = node

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _ensure_count_node(self, count: int, after: Node) -> Node:
        current = after.next
        while current is not self.tail and current.count < count:
            current = current.next
        if current is not self.tail and current.count == count:
            return current
        bucket = Node(count)
        self._insert_after(current.prev, bucket)
        return bucket

    def inc(self, key: str) -> None:
        if key in self.key_nodes:
            bucket = self.key_nodes[key]
            bucket.keys.remove(key)
            next_bucket = self._ensure_count_node(bucket.count + 1, bucket)
            next_bucket.keys.add(key)
            self.key_nodes[key] = next_bucket
            if not bucket.keys:
                self._remove(bucket)
            return

        bucket = self._ensure_count_node(1, self.head)
        bucket.keys.add(key)
        self.key_nodes[key] = bucket

    def dec(self, key: str) -> None:
        bucket = self.key_nodes[key]
        bucket.keys.remove(key)
        if bucket.count == 1:
            del self.key_nodes[key]
        else:
            prev_bucket = self._ensure_count_node(bucket.count - 1, self.head)
            prev_bucket.keys.add(key)
            self.key_nodes[key] = prev_bucket
        if not bucket.keys:
            self._remove(bucket)

    def getMaxKey(self) -> str:
        bucket = self.tail.prev
        if bucket is self.head:
            return ""
        return next(iter(bucket.keys))

    def getMinKey(self) -> str:
        bucket = self.head.next
        if bucket is self.tail:
            return ""
        return next(iter(bucket.keys))
